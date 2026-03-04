#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

# Import the conversion logic from the project's module.
try:
    from converter import convert_markdown_to_html
except Exception as exc:  # pragma: no cover
    sys.stderr.write(f"Failed to load converter module: {exc}\n")
    sys.exit(1)


def parse_arguments() -> argparse.Namespace:
    """Define and parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog="md2html",
        description="Convert Markdown files into styled HTML pages.",
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the source Markdown file or directory containing Markdown files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Directory where generated HTML files will be written. "
             "Defaults to the same directory as the source file(s).",
    )
    parser.add_argument(
        "-t",
        "--title",
        default=None,
        help="Optional title for the generated HTML pages.",
    )
    parser.add_argument(
        "-s",
        "--stylesheet",
        type=Path,
        default=None,
        help="Path to a CSS file to link in the generated HTML. "
             "If omitted, no external stylesheet will be referenced.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print progress information during conversion.",
    )
    return parser.parse_args()


def process_single_file(src: Path, dst_dir: Path, title: str | None, css_path: Path | None) -> None:
    """Convert a single Markdown file to HTML."""
    if not src.is_file():
        raise FileNotFoundError(f"Source file not found: {src}")
    output_path = dst_dir / f"{src.stem}.html"
    convert_markdown_to_html(
        markdown_path=src,
        html_path=output_path,
        title=title,
        stylesheet=css_path,
    )
    return


def process_directory(src_dir: Path, dst_dir: Path, title: str | None, css_path: Path | None) -> None:
    """Recursively convert all Markdown files in a directory."""
    for md_file in src_dir.rglob("*.md"):
        process_single_file(md_file, dst_dir, title, css_path)


def main() -> int:
    args = parse_arguments()

    # Resolve paths to absolute form
    source = args.source.resolve()
    output_dir = args.output.resolve() if args.output else source.parent
    stylesheet = args.stylesheet.resolve() if args.stylesheet else None

    try:
        if source.is_file():
            process_single_file(source, output_dir, args.title, stylesheet)
        elif source.is_dir():
            process_directory(source, output_dir, args.title, stylesheet)
        else:
            sys.stderr.write(f"Source path is neither a file nor a directory: {source}\n")
            return 1
    except Exception as exc:
        sys.stderr.write(f"Error during conversion: {exc}\n")
        return 1

    if args.verbose:
        print(f"Conversion completed. HTML files written to: {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())