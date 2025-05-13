# FileWorks

**FileWorks** is a Python-based utility suite designed for efficient file system operations, including file synchronization, transformation, and reporting. It provides a set of scripts to automate common file management tasks, making it easier to handle large volumes of files with minimal manual intervention.

**And the most of all:** A simple CLI tool to move and rename files with customizable filtering and transformation.

## Features

* **File Synchronization**: Keep directories in sync by copying or moving files between them.
* **File Transformation**: Rename files based on custom rules, such as transliteration and cleaning.
* **File Reporting**: Generate reports on file discrepancies and changes.
* **Utility Scripts**: Additional scripts for file system operations and comparisons.

## Folder Structure (To Be Updated)

The repository is organized as follows:

```

fileworks/
├── core/                        # Core utilities and configurations
│   ├── __init__.py
│   ├── config.py                # Configuration settings
│   └── constants.py             # Constant values and mappings
├── mover/                       # IO-Moving Functionality
├── scripts/                     # Own Legacy
├── tools/                       # Utility functions and transformers
│   ├── __init__.py
│   ├── filters.py               # File name filters
│   ├── logger.py                # Renaming logger
│   ├── transformers.py          # File name transformers
├── utils/                       # Helpers
│   ├── compare.py               # Compare with hashsums
│   ├── date.py                  # Date-time
│   ├── io.py                    # For moving and renaming files
│   ├── name.py                  # From camel to snake case
│   ├── stats.py                 # Files counter
│   └── string.py                # For strings
├── main.py                      # Entry point
├── .env.example                 # Example environment variables
├── .gitignore                   # Git ignore file
├── LICENSE.md                   # License information
├── README.md                    # Project overview and documentation
└── requirements.txt             # Python dependencies
```

---

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/avtomatik/fileworks.git
cd fileworks
pip install --no-cache-dir -r requirements.txt
cp .env.example .env
# Then Make Necessary Amendments to .env
```

---

## Usage

Run the CLI tool with Python, calling the main module:

```bash
python3 -m fileworks.fileworks.main [path] [-e EXTENSIONS ...] [-v]
```

* `path` (optional):
  Directory path to process. Defaults to the current working directory if not provided.

* `-e`, `--extensions` (optional):
  Filter files by one or more file extensions (without the leading dot).
  Example: `-e csv txt` will only process `.csv` and `.txt` files.

* `-v`, `--verbose` (optional):
  Enable verbose output, printing info about the processing steps.

---

## Examples

Process **all files** in the current directory:

```bash
python3 -m fileworks.fileworks.main
```

Process **only `.csv` and `.txt` files** in the current directory:

```bash
python3 -m fileworks.fileworks.main -e csv txt
```

Process **all files** in a specific directory:

```bash
python3 -m fileworks.fileworks.main /path/to/directory
```

Process **only `.csv` files** in a specific directory with verbose output:

```bash
python3 -m fileworks.fileworks.main /path/to/directory -e csv -v
```

---

## Notes

* File extensions passed to `-e` should **not** include the leading dot (`.`).
* If no extensions are specified, all files in the directory are processed.
* The tool processes only **regular files**, ignoring directories.

---

## Help

You can always run the tool with `-h` or `--help` to get usage information:

```bash
python3 -m fileworks.fileworks.main -h
```

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
