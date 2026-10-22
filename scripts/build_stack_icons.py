"""Build compact, self-hosted tech-stack icon strips from local SVG marks."""

from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOURCES = ASSETS / "brand-icons"


def tile(name: str, x: int) -> str:
    frame = f'<rect x="{x}" y="0" width="48" height="48" rx="10" fill="#242938"/>'
    if name == "faiss":
        # A custom vector-search glyph, not an official FAISS logo.
        mark = (
            f'<g transform="translate({x + 8} 8)" fill="none" stroke="#62C8FF" '
            'stroke-linecap="round" stroke-linejoin="round" stroke-width="2.8">'
            '<path d="M3 5h19M3 12h16M3 19h11"/>'
            '<circle cx="22" cy="22" r="6"/>'
            '<path d="m26.5 26.5 5 5"/>'
            '</g>'
        )
    else:
        root = ElementTree.parse(SOURCES / f"{name}.svg").getroot()
        path = next(element for element in root.iter() if element.tag.endswith("path"))
        fill = root.attrib["fill"]
        mark = (
            f'<path transform="translate({x + 9} 9) scale(1.25)" '
            f'fill="{fill}" d="{path.attrib["d"]}"/>'
        )
    return frame + mark


def write_strip(filename: str, names: list[str], title: str) -> None:
    width = 48 * len(names) + 8 * (len(names) - 1)
    tiles = "\n  ".join(tile(name, index * 56) for index, name in enumerate(names))
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="48" '
        f'viewBox="0 0 {width} 48" role="img">\n'
        f'  <title>{title}</title>\n  {tiles}\n</svg>\n'
    )
    (ASSETS / filename).write_text(svg, encoding="utf-8")


write_strip("stack-streamlit.svg", ["streamlit"], "Streamlit")
write_strip(
    "stack-ai-extra.svg",
    ["huggingface", "langchain", "langgraph", "faiss", "vllm"],
    "Hugging Face, LangChain, LangGraph, FAISS, and vLLM",
)
