import xml.etree.ElementTree as ET
import re, copy, subprocess, tempfile
import shortuuid
from typing import Optional
import pdftowrite.utils as utils
from picosvg.svg import SVG
from subprocess import DEVNULL
from pathlib import Path
from abc import ABC, abstractmethod

SVG_NS = 'http://www.w3.org/2000/svg'
XLINK_NS = 'http://www.w3.org/1999/xlink'

ET.register_namespace('', SVG_NS)
ET.register_namespace('xlink', XLINK_NS)

class SizeBox(ABC):
    @property
    @abstractmethod
    def size_element(self) -> ET.Element:
        return None

    @property
    def x(self) -> str:
        return self.size_element.get('x', '0').strip()

    @x.setter
    def x(self, val: str):
        self.size_element.set('x', val)

    @property
    def y(self) -> str:
        return self.size_element.get('y', '0').strip()

    @y.setter
    def y(self, val: str):
        self.size_element.set('y', val)

    @property
    def width(self) -> str:
        return self.size_element.get('width').strip()

    @width.setter
    def width(self, val: str):
        self.size_element.set('width', val)

    @property
    def height(self) -> str:
        return self.size_element.get('height').strip()

    @height.setter
    def height(self, val: str):
        self.size_element.set('height', val)

    @property
    def viewbox(self) -> Optional[str]:
        return self.size_element.get('viewBox', None)

    @viewbox.setter
    def viewbox(self, value: Optional[str]):
        if value is None:
            self.size_element.pop('viewBox', None)
        else:
            self.size_element.set('viewBox', value)

class Background(SizeBox):
    def __init__(self, page_num, svg, text_layer_svg, compat_mode=True, uniquify=True):
        self.page_num = page_num
        self.suffix = '-' + shortuuid.uuid()[:7] + '-p' + str(self.page_num)
        self.__process_svg(svg, text_layer_svg, compat_mode, uniquify)
        self.tree.getroot().set('class', self.tree.getroot().get('class', '') + ' page-background')

    @property
    def size_element(self) -> ET.Element:
        return self.tree.getroot()

    @property
    def svg(self) -> str:
        return ET.tostring(self.tree.getroot(), encoding='unicode')

    def __process_svg(self, svg, text_layer_svg, compat_mode, uniquify) -> None:
        svg = re.sub(r'<\?xml[^(\?>)]*\?>', '', svg)
        self.tree = ET.ElementTree( ET.fromstring(svg) )
        self.__remove_metadata()
        self.__remove_inkscape_styles()
        if compat_mode:
            self.__simplify()
            self.__remove_masked_rects()
            self.__convert_masked_images()
        if uniquify: self.__uniquify()
        if text_layer_svg:
            self.text_layer = self.__create_text_layer(text_layer_svg)
            self.tree.getroot().append(self.text_layer)
        else:
            self.text_layer = None

    def __remove_metadata(self):
        root = self.tree.getroot()
        for el in root:
            _, _, tag = el.tag.partition('}')
            if tag == 'metadata':
                root.remove(el)
                break

    def __remove_inkscape_styles(self):
        for el in self.tree.iter():
            if 'style' in el.attrib:
                style = el.get('style')
                style = re.sub(r'[^;]*inkscape[^;]*(;|$)', '', style)
                el.set('style', style)

    def __simplify(self):
        try:
            self.__tree_map = { el.get('id', ''): el for el in self.tree.iter() }
            self.__parent_map = { c:p for p in self.tree.iter() for c in p }

            clip_groups = self.__get_clip_root_groups()
            clip_paths = self.__get_clip_paths()
            attachments = {}
            for g in clip_groups:
                attachs = self.__get_attachments_for(g)
                attachments.update(attachs)

            svg = ET.Element('svg')
            defs = ET.Element('defs')
            for el in clip_paths:
                dup = copy.deepcopy(el)
                defs.append(dup)
            for el in attachments.values():
                dup = copy.deepcopy(el)
                defs.append(dup)
            svg.append(defs)
            for el in clip_groups:
                dup = copy.deepcopy(el)
                svg.append(dup)

            svg_tree = ET.ElementTree(svg)
            self.__parent_map = { c:p for p in svg_tree.iter() for c in p }
            self.__remove_images(svg)
            svg_text = ET.tostring(svg, encoding='unicode')

            picosvg = SVG.fromstring(svg_text).topicosvg()
            picosvg_text = picosvg.tostring()
            picosvg_tree = ET.ElementTree( ET.fromstring(picosvg_text) )

            picosvg_paths = picosvg_tree.findall('.//{%s}path' % SVG_NS)
            picosvg_paths_map = { el.get('id', ''): el for el in picosvg_paths}

            paths = []
            for g in clip_groups:
                paths += g.findall('.//{%s}path' % SVG_NS)
            for el in paths:
                id = el.get('id', '')
                pico_path = picosvg_paths_map[id]
                d = pico_path.get('d', '')
                el.set('d', d)
            self.__tree_map = None
            self.__parent_map = None
        except:
            pass

    def __get_clip_root_groups(self) -> list[ET.Element]:
        result = []
        for el in self.tree.iter():
            if 'clip-path' not in el.attrib: continue
            if self.__group_has_clip_ancestors(el): continue
            result.append(el)
        return result

    def __group_has_clip_ancestors(self, el: ET.Element) -> bool:
        parent = self.__parent_map.get(el)
        if parent is None: return False
        if 'clip-path' in parent.attrib: return True
        return self.__group_has_clip_ancestors(parent)

    def __get_clip_paths(self) -> list[ET.Element]:
        result = []
        for el in self.tree.iter():
            _, _, tag = el.tag.partition('}')
            if tag == 'clipPath':
                result.append(el)
        return result

    def __get_attachments_for(self, el: ET.Element) -> dict[str,ET.Element]:
        href_els = el.findall('.//*[@{%s}href]' % XLINK_NS)
        result = {}
        for href_el in href_els:
            match = re.search(r'#\s*([^\s]+)', href_el.get('{%s}href' % XLINK_NS))
            id = match.group(1)
            target_el = self.__tree_map[id]
            _, _, target_tag = target_el.tag.partition('}')
            if target_tag != 'image':
                result[id] = target_el
        return result

    def __remove_images(self, el: ET.Element) -> None:
        href_els = el.findall('.//*[@{%s}href]' % XLINK_NS)
        for href_el in href_els:
            match = re.search(r'#\s*([^\s]+)', href_el.get('{%s}href' % XLINK_NS))
            id = match.group(1)
            target_el = self.__tree_map[id]
            _, _, target_tag = target_el.tag.partition('}')
            if target_tag == 'image':
                self.__parent_map[href_el].remove(href_el)
        image_els = el.findall('.//{%s}image' % XLINK_NS)
        for image_el in image_els:
            self.__parent_map[image_el].remove(image_el)

    def __remove_masked_rects(self):
        self.__parent_map = { c:p for p in self.tree.iter() for c in p }
        rects = self.tree.getroot().findall('.//{%s}rect[@mask]' % SVG_NS)
        for rect in rects:
            self.__parent_map[rect].remove(rect)
        self.__parent_map = None

    def __convert_masked_images(self):
        self.__tree_map = { el.get('id', ''): el for el in self.tree.iter() }
        self.__parent_map = { c:p for p in self.tree.iter() for c in p }

        uses = self.tree.getroot().findall('.//{%s}use[@{%s}href][@mask]' % (SVG_NS, XLINK_NS))
        for use in uses:
            href = use.get('{%s}href' % XLINK_NS)
            href_id = utils.pattern_get(r'#\s*([^\s]+)', href, 1)
            href_el = self.__tree_map[href_id]
            if utils.tagname(href_el) != 'image': continue

            mask = use.get('mask')
            mask_id = utils.pattern_get(r'url\s*\(\s*#\s*(.+?)\s*\)', mask, 1)
            mask_el = self.__tree_map[mask_id]
            mask_use_el = mask_el.find('.//{%s}use[@{%s}href]' % (SVG_NS, XLINK_NS))
            if mask_use_el is None: continue
            mask_use_el_href_id = utils.pattern_get(r'#\s*([^\s]+)', mask_use_el.get('{%s}href' % XLINK_NS), 1)
            mask_use_el_href_el = self.__tree_map[mask_use_el_href_id]

            image_data_uri = href_el.get('{%s}href' % XLINK_NS, '')
            mask_data_uri = mask_use_el_href_el.get('{%s}href' % XLINK_NS, '')
            if not image_data_uri or not mask_data_uri: continue
            img_header, img_suffix, img_data = utils.decode_image_uri(image_data_uri)
            mask_header, mask_suffix, mask_data = utils.decode_image_uri(mask_data_uri)
            if not img_header or not mask_header: continue

            with tempfile.TemporaryDirectory() as tmpdir:
                img_path = str(Path(tmpdir) / f'image{img_suffix}')
                mask_path = str(Path(tmpdir) / f'mask{mask_suffix}')
                comb_path = str(Path(tmpdir) / f'comb.png')
                with open(img_path, 'wb') as f:
                    f.write(img_data)
                    f.flush()
                with open(mask_path, 'wb') as f:
                    f.write(mask_data)
                    f.flush()
                subprocess.check_call(
                    ['convert', img_path, mask_path, '-compose', 'CopyOpacity', '-composite', comb_path],
                    stdout=DEVNULL, stderr=DEVNULL)
                with open(comb_path, 'rb') as f:
                    data = f.read()

            encoded = utils.encode_image_uri(data)
            data_uri = 'data:image/png;base64,' + encoded
            href_el.set('{%s}href' % XLINK_NS, data_uri)
            use.attrib.pop('mask')

        self.__tree_map = None
        self.__parent_map = None

    def __uniquify(self):
        for el in self.tree.iter():
            self.__uniquify_element(el, self.suffix)

    def __uniquify_element(self, el: ET.Element, suffix: str):
        _, _, tag = el.tag.partition('}')
        if 'id' in el.attrib:
            el.attrib['id'] += suffix
        if tag == 'use' and ('{%s}href' % XLINK_NS) in el.attrib:
            el.attrib['{%s}href' % XLINK_NS] += suffix
        self.__uniquify_url_attribs(el, suffix)

    def __uniquify_url_attribs(self, el: ET.Element, suffix: str):
        for k, v in el.attrib.items():
            newv = re.sub(r'url\s*\(\s*#\s*(.+?)\s*\)', lambda m: f'url(#{m.group(1) + suffix})', v)
            el.set(k, newv)

    def __create_text_layer(self, text_layer_svg) -> ET.Element:
        tree = ET.ElementTree( ET.fromstring(text_layer_svg) )
        text_layer_vb = tree.getroot().get('viewBox')
        text_layer_vb_width = utils.viewbox_vals(text_layer_vb)[2]
        text_layer_vb_height = utils.viewbox_vals(text_layer_vb)[3]

        self.__parent_map = { c:p for p in tree.iter() for c in p }
        group = self.__create_text_group(tree)
        self.__parent_map = None

        el = ET.Element('svg')
        el.set('id', 'text-layer' + self.suffix)
        el.set('class', el.get('class', '') + ' pdftowrite-text-layer')
        el.set('width', utils.viewbox_vals(self.viewbox)[2])
        el.set('height', utils.viewbox_vals(self.viewbox)[3])
        el.set('viewBox', f'0 0 {text_layer_vb_width} {text_layer_vb_height}')
        el.append(group)
        return el

    def __create_text_group(self, tree) -> ET.Element:
        group = ET.Element('g')
        g = tree.getroot().find('./{%s}g[last()]' % SVG_NS)
        if 'transform' in g.attrib:
            group.set('transform', g.get('transform'))

        text_els = self.__get_text_elements(tree)
        for text_el in text_els:
            style = text_el.get('style', '')
            style = self.__style_attr(style, 'fill-opacity', '0')
            style = self.__style_attr(style, 'stroke', 'none')
            text_el.set('style', style)
            group.append(text_el)
        return group

    def __get_text_elements(self, tree) -> list[ET.Element]:
        result = []
        texts = tree.getroot().findall('.//{%s}text' % SVG_NS)
        for text in texts:
            for el in text.iter():
                el.attrib.pop('id', None)
                el.attrib.pop('clip-path', None)
            parent_g = self.__parent_map[text]
            if parent_g and 'transform' in parent_g.attrib and 'transform' not in text.attrib:
                num_children = len(parent_g.findall('./{%s}text' % SVG_NS))
                if num_children == 1:
                    text.set('transform', parent_g.get('transform'))
            result.append(text)
        return result

    def __style_attr(self, style, name, val):
        pattern = rf'({name}\s*:\s*)([^;]+?)(;|$)'
        regex = re.compile(pattern)
        if not regex.search(style):
            return style + f';{name}:{val};'
        else:
            return regex.sub(rf'{name}:{val};', style)

class Page(SizeBox):
    def __init__(self, page_num, svg):
        self.page_num = page_num
        self.__process_svg(svg)

    @property
    def size_element(self) -> ET.Element:
        return self.tree.getroot()

    @property
    def svg(self) -> str:
        return ET.tostring(self.tree.getroot(), encoding='unicode')

    @property
    def background(self) -> Optional[SizeBox]:
        if self.__background:
            return Page._BackgroundBox(self.__background)
        else:
            return None

    @property
    def write_content(self) -> ET.Element:
        return utils.find_elements_by_class(self.tree, 'write-content')[0]

    @property
    def ruleline(self) -> ET.Element:
        return utils.find_elements_by_class(self.tree, 'ruleline')[0]

    def remove_ruleline(self) -> None:
        write_content = self.write_content
        ruleline = self.ruleline
        write_content.remove(ruleline)

    @property
    def pdf_file(self) -> Optional[str]:
        return self.ruleline.get('data-pdf-file', None)

    @property
    def pdf_page(self) -> Optional[int]:
        ruleline = self.ruleline
        if 'data-pdf-file' in ruleline.attrib:
            return int( ruleline.get('data-pdf-page') )
        else:
            return None

    def __process_svg(self, svg) -> None:
        svg = re.sub(r'<\?xml[^(\?>)]*\?>', '', svg)
        self.tree = ET.ElementTree( ET.fromstring(svg) )
        bgs = utils.find_elements_by_class(self.tree, 'page-background')
        if bgs:
            self.__background = bgs[0]
        else:
            ruleline = utils.find_elements_by_class(self.tree, 'ruleline')[0]
            bg = ruleline.find('./{%s}svg' % SVG_NS)
            self.__background = bg # Optional

    class _BackgroundBox(SizeBox):
        def __init__(self, element: ET.Element):
            self.element = element

        @property
        def size_element(self) -> ET.Element:
            return self.element

class Document:
    def __init__(self, svg: str, page_nums: set[int]):
        self.tree = ET.ElementTree( ET.fromstring(svg) )
        self.pages = []
        page_els = self.tree.getroot().findall('./{%s}svg' % SVG_NS)
        num = 0
        for page_el in page_els:
            num += 1
            if 'write-page' not in page_el.get('class', ''): continue
            if num not in page_nums: continue
            page_svg = ET.tostring(page_el, encoding='unicode')
            page = Page(num, page_svg)
            self.pages.append(page)
        if num <= 0: raise Exception('Document has no pages')

def num_pages(svg: str) -> int:
    tree = ET.ElementTree( ET.fromstring(svg) )
    page_els = tree.getroot().findall('./{%s}svg' % SVG_NS)
    num = 0
    for page_el in page_els:
        if 'write-page' not in page_el.get('class', ''): continue
        num += 1
    return num
