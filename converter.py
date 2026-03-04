import pathlib
from typing import Union

import markdown  # type: ignore


class MarkdownConverter:
    """
    Convert Markdown content into a styled HTML page.
    """

    def __init__(self, css_path: Union[str, pathlib.Path] | None = None):
        """
        :param css_path: Path to an external CSS file. If omitted, a minimal default style is used.
        """
        self.css_path = pathlib.Path(css_path) if css_path else None
        self._default_css = (
            "body {font-family: Arial, sans-serif; margin: 2rem; background:#f8f9fa;} "
            "h1,h2,h3,h4,h5,h6 {color:#343a40;} pre {background:#e9ecef;padding:.5rem;border-radius:.25rem;} "
            "code {font-family: monospace;}"
        )

    def _read_file(self, path: Union[str, pathlib.Path]) -> str:
        """Read text from a file."""
        return pathlib.Path(path).read_text(encoding="utf-8")

    def _write_file(self, path: Union[str, pathlib.Path], content: str) -> None:
        """Write text to a file, creating parent directories if needed."""
        p = pathlib.Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def _load_css(self) -> str:
        """Return CSS content from the specified file or default style."""
        if self.css_path and self.css_path.is_file():
            return self._read_file(self.css_path)
        return self._default_css

    def convert(
        self,
        markdown_source: Union[str, pathlib.Path],
        output_html: Union[str, pathlib.Path],
    ) -> None:
        """
        Convert a Markdown file to an HTML file with styling.

        :param markdown_source: Path to the source Markdown file.
        :param output_html: Destination path for the generated HTML file.
        """
        md_text = self._read_file(markdown_source)
        html_body = markdown.markdown(md_text, extensions=["extra", "toc"])
        css = self._load_css()

        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{pathlib.Path(markdown_source).stem}</title>
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>"""

        self._write_file(output_html, full_html)
<|reserved_200016|>#!/usr/bin/env python3
import argparse
from pathlib import Path

from converter import MarkdownConverter


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to styled HTML pages."
    )
    parser.add_argument("input", type=Path, help="Markdown file to convert")
    parser.add_argument("-o", "--output", type=Path, help="Output HTML file")
    parser.add_argument("--css", type=Path, help="Custom CSS stylesheet")

    args = parser.parse_args()

    output_path = (
        args.output
        if args.output
        else Path(args.input.with_suffix(".html").name)
    )

    converter = MarkdownConverter(css_path=args.css)
    converter.convert(args.input, output_path)

    print(f"Converted {args.input} → {output_path}")


if __name__ == "__main__":
    main()