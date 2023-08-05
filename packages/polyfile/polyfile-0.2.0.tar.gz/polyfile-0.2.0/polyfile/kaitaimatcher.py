import base64
from typing import Dict, Iterator, List, Tuple, Type

from kaitaistruct import KaitaiStructError

from .kaitai.parser import ASTNode, KaitaiParser, KaitaiStruct, RootNode
from .kaitai.parsers.gif import Gif
from .kaitai.parsers.jpeg import Jpeg
from .kaitai.parsers.pcap import Pcap
from .kaitai.parsers.png import Png
from .kaitai.parsers.sqlite3 import Sqlite3
from .polyfile import submatcher, InvalidMatch, Match, Submatch

KAITAI_TRID_MAPPING: Dict[str, Type[KaitaiStruct]] = {
    "bitmap-gif.trid.xml": Gif,
    "bitmap-gif-anim.trid.xml": Gif,
    "bitmap-jpeg.trid.xml": Jpeg,
    "bitmap-png.trid.xml": Png,
    "pcap-ext-be.trid.xml": Pcap,
    "pcap-ext-le.trid.xml": Pcap,
    "acp-le.trid.xml": Pcap,
    "sqlite-3x.trid.xml": Sqlite3
}
IMAGE_MIMETYPES: Dict[Type[KaitaiStruct], str] = {
    Gif: "image/gif",
    Jpeg: "image/jpeg",
    Png: "image/png"
}


def ast_to_matches(ast: RootNode, parent: Match) -> Iterator[Submatch]:
    stack: List[Tuple[Match, ASTNode]] = [(parent, ast)]
    while stack:
        parent, node = stack.pop()

        new_node = Submatch(
            name=node.name,
            match_obj=node.raw_value,
            relative_offset=node.start,
            length=len(node.segment),
            parent=parent
        )

        if node is ast and node.obj.__class__ in IMAGE_MIMETYPES:  # type: ignore
            # this is an image type, so create a preview
            new_node.img_data = f"data:{IMAGE_MIMETYPES[kaitai_def]};base64," \
                                f"{base64.b64encode(ast.raw_value).decode('utf-8')}"

        yield new_node
        stack.extend(reversed([(new_node, c) for c in node.children]))


for trid_def, kaitai_def in KAITAI_TRID_MAPPING.items():
    @submatcher(trid_def)
    class KaitaiMatcher(Match):
        def submatch(self, file_stream):
            try:
                ast = KaitaiParser(kaitai_def).parse(file_stream).ast
            except (Exception, KaitaiStructError):
                raise InvalidMatch()
            yield from ast_to_matches(ast, parent=self)
