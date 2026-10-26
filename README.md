# Tenviora Technologies

## Experimental Gematria Primus-Inspired Cryptanalysis Engine

### Overview

This project is an experimental Python research tool exploring Gematria Primus-inspired character mapping and cryptanalysis techniques.

The software is designed for algorithm experimentation, configurable parameters, and reproducible testing.

### Research Disclaimer

The default key is artificial and is not a recovered Cicada 3301 key. This project does not claim to solve Cicada 3301. Ciphertext provenance, cipher methods, and any proposed results require independent verification.

### Requirements

- Python 3.9 or later recommended.
- The current script uses Python standard-library modules, including `argparse` and `pathlib`.

### Installation

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project directory.

### Usage

Display available command-line options:

```bash
python script1.py --help
```

Run the built-in self-tests:

```bash
python script1.py --test
```

Generate a research report:

```bash
python script1.py --report master_report.txt
```

Additional options include configurable transposition columns, Fibonacci starting values, and a numerical key. Run the help command above to see the available options and defaults.

### Project Files

- `script1.py` — primary research script.
- `master_report.txt` — research report.
- `METHODOLOGY.md` — research methodology and assumptions.
- `TESTS.md` — testing procedures and results.
- `LICENSE` — copyright and usage terms.

### Testing Status

The author reports that the built-in self-tests passed. This indicates that the implemented tests completed successfully; it does not independently establish cryptographic correctness or a solution to Cicada 3301.

### Author

**Tiffany Jean Mathias Bowman**  
Tenviora Technologies

### Project Status

Experimental research software. Results should be independently verified before being treated as established findings.