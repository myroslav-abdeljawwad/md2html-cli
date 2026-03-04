# md2html-cli  
**CLI tool to convert Markdown files into styled HTML pages**

---

## Features
- Convert any `.md` file to a self‑contained, CSS‑styled HTML page.
- Supports GitHub‑flavored Markdown (tables, code fences, etc.).
- Auto‑generates a `<title>` tag from the first heading or filename.
- Optional custom CSS via `--style <path>`.
- One‑command usage with minimal dependencies.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/md2html-cli.git
cd md2html-cli

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
# Basic conversion
python main.py example.md

# Output to a specific file
python main.py example.md --output output.html

# Use custom CSS
python main.py example.md --style custom.css

# Show help
python main.py --help
```

The generated HTML will be placed in the same directory as the source Markdown unless `--output` is specified.

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-x`).
3. Commit your changes with clear messages.
4. Push to your fork and open a Pull Request.

Please run tests before submitting:

```bash
pytest
```

All contributions are welcome—feel free to submit issues or pull requests!

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Author

**Myroslav Mokhammad Abdeljawwad**

*Python developer & open‑source enthusiast.*