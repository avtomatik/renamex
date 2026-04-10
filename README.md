# renamex

[![CI](https://github.com/avtomatik/renamex/actions/workflows/main.yml/badge.svg)](https://github.com/avtomatik/renamex/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org)
[![crates.io](https://img.shields.io/crates/v/renamex.svg)](https://crates.io/crates/renamex)

**renamex** is a fast and reliable command-line tool for cleaning, normalizing, and renaming files in bulk.

It provides safe and predictable transformations, including transliteration, string normalization, extension-based filtering, and recursive directory processing.

---

## Features

- Filename normalization
  - Removes invalid characters
  - Replaces separators with underscores
  - Produces consistent file names

- Transliteration
  - Converts Cyrillic characters to Latin equivalents

- Extension filtering
  - Processes only selected file types

- Recursive processing
  - Traverse directories recursively with `--recursive`

- Safe renaming
  - Skips unchanged files
  - Prevents overwriting existing files via auto-uniquing

- Parallel processing
  - Efficient handling of large directories using multithreading

- Dry-run mode
  - Preview changes before applying them

---

## Installation

### From crates.io (recommended)

```bash
cargo install renamex
```

---

### From source

```bash
git clone https://github.com/avtomatik/renamex.git
cd renamex
cargo install --path .
```

---

## Usage

```bash
renamex [PATH] [OPTIONS]
```

### Arguments

* `PATH` (optional)
  Directory to process. Defaults to the current working directory.

---

### Options

* `-e, --extensions <EXT>...`
  Filter files by extension (without leading dot)

* `-r, --recursive`
  Recursively process all subdirectories

* `-v, --verbose`
  Print detailed processing output

* `--dry-run`
  Show planned changes without modifying files

---

## Examples

### Process all files in current directory

```bash
renamex
```

---

### Process specific extensions

```bash
renamex -e csv txt
```

---

### Process a directory

```bash
renamex /path/to/directory
```

---

### Recursive processing

```bash
renamex /path/to/directory -r
```

---

### Preview changes (safe mode)

```bash
renamex --dry-run -v
```

---

### Recursive + filter + verbose

```bash
renamex /path/to/directory -r -e csv txt -v
```

---

## Example

### Input

```
отчет_январь.csv
отчет_февраль.csv
пример.txt
```

### Command

```bash
renamex -e csv txt -v
```

### Output

```
отчет_январь.csv -> otchet_yanvar.csv
отчет_февраль.csv -> otchet_fevral.csv
пример.txt -> primer.txt
```

---

## Behavior

* Processes only regular files
* Supports recursive directory traversal (`--recursive`)
* Renames files in place
* Never overwrites existing files (auto-resolves collisions)
* Skips files that do not change
* Skips hidden files (starting with `.`)

---

## Installation from crates.io

Once installed via:

```bash
cargo install renamex
```

you can run:

```bash
renamex --help
```

---

## Development

```bash
cargo build --release
cargo test
cargo fmt --check
cargo clippy -- -D warnings
```

---

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

---

## License

MIT License. See `LICENSE.md` for details.
