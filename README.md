# FileWorks

**FileWorks** is a Python utility suite for efficient file system operations, including moving, renaming, filtering, and transforming files. It provides a simple CLI tool to automate common file management tasks and handle large volumes of files with minimal manual intervention.

---

## Features

* **File Transformation**: Rename files with customizable rules, such as transliteration and string cleaning.
* **File Filtering**: Process only files with certain extensions.
* **File Renaming**: Move and rename files safely and efficiently.
* **Utility Functions**: Core modules for file handling, string cleaning, and file system operations.

---

## Repository Structure

```
fileworks/
├── core/                        # Core utilities and constants
│   └── constants.py             # Constant values and mappings
├── interfaces/                  # Abstractions and adapters
│   ├── adapters.py              # File moving adapter
│   └── protocols.py             # Interface definitions
├── tools/                       # Utility modules for filtering, cleaning, and transforming
│   ├── cleaners.py              # File name cleaning and transliteration
│   ├── cli.py                   # Command-line interface
│   ├── filenames.py             # File name helpers
│   ├── filters.py               # File filtering rules
│   ├── loggers.py               # Logging for file operations
│   ├── movers.py                # File moving/renaming logic
│   └── transformers.py          # File name transformers
├── __main__.py                  # Entry point for `python3 -m fileworks`
├──.github
│   └── workflows/
│       └── main.yml             # CI/CD pipeline
├── requirements-dev.txt         # Dev dependencies: ruff, mypy, pytest
├── pyproject.toml               # Project info & Ruff configuration
├── LICENSE.md
└── README.md
```

---

## Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/avtomatik/fileworks.git
cd fileworks
```

*(Optionally, create a virtual environment and install dependencies if required.)*

---

## Usage

Run the CLI tool with Python:

```bash
python3 -m fileworks [path] [-e EXTENSIONS ...]
```

### Arguments

* `path` (optional):
  Directory to process. Defaults to the **current working directory** if not provided.

* `-e`, `--extensions` (optional):
  Filter files by one or more file extensions (without the leading dot).
  Example: `-e csv txt` will only process `.csv` and `.txt` files.

---

### Examples

Process **all files** in the current directory:

```bash
python3 -m fileworks
```

Process **only `.csv` and `.txt` files** in the current directory:

```bash
python3 -m fileworks -e csv txt
```

Process **all files** in a specific directory:

```bash
python3 -m fileworks /path/to/directory
```

Process **only `.csv` files** in a specific directory:

```bash
python3 -m fileworks /path/to/directory -e csv
```

---

## Getting Started (Before & After)

Suppose you have a directory with the following files:

```
~/Downloads/TestFiles/
├── отчет_январь.csv
├── отчет_февраль.csv
├── пример.txt
├── .hidden_file
```

Running FileWorks with:

```bash
python3 -m fileworks ~/Downloads/TestFiles -e csv txt
```

will process the files using the cleaning, transliteration, and trimming rules. After processing, the directory may look like this:

```
~/Downloads/TestFiles/
├── otchet_yanvar.csv
├── otchet_fevral.csv
├── primer.txt
├── .hidden_file
```

**What happened:**

* Cyrillic file names were transliterated to Latin characters.
* Spaces or invalid characters were replaced with underscores.
* Only `.csv` and `.txt` files were processed.
* Hidden files (starting with `.`) are ignored by default.

This gives users a quick understanding of the transformations FileWorks performs.

---

## Notes


* File extensions passed to `-e` should **not** include the leading dot (`.`).
* If no extensions are specified, all files in the directory are processed.
* The tool processes only **regular files**, ignoring directories.
* Use `--help` to display usage information:

```bash
python3 -m fileworks --help
```

---

## Contributing

Contributions are welcome! Fork the repository, create a branch, and submit a pull request with your changes.

---

## License

This project is licensed under the MIT License — see [LICENSE.md](LICENSE.md) for details.

---
