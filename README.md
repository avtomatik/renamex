# renamex

[![CI](https://github.com/avtomatik/renamex/actions/workflows/main.yml/badge.svg)](https://github.com/avtomatik/renamex/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org)

**renamex** is a fast and reliable command-line tool for cleaning, normalizing, and renaming files in bulk.

It provides safe and predictable transformations, including transliteration, string normalization, and extension-based filtering.

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

- Safe renaming
  - Skips unchanged files
  - Prevents overwriting existing files

- Parallel processing
  - Efficient handling of large directories

- Dry-run mode
  - Preview changes before applying them

---

## Installation

### From source

```bash
git clone https://github.com/avtomatik/renamex.git
cd renamex
cargo install --path .
````

### From crates.io (after publishing)

```bash
cargo install renamex
```

---

## Usage

```bash
renamex [path] [OPTIONS]
```

### Arguments

* `path` (optional)
  Directory to process. Defaults to the current working directory.

### Options

* `-e, --extensions <EXT>...`
  Filter files by extension (without leading dot)

* `-v, --verbose`
  Print detailed processing output

* `--dry-run`
  Show planned changes without modifying files

---

## Examples

### Process all files

```bash
renamex
```

### Process specific extensions

```bash
renamex -e csv txt
```

### Process a directory

```bash
renamex /path/to/directory
```

### Preview changes

```bash
renamex --dry-run -v
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
* Renames files in place
* Never overwrites existing files
* Skips files that do not change

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
