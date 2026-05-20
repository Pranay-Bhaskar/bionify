<div align="center">

  <img src="https://raw.githubusercontent.com/Pranay-Bhaskar/fovea/main/assets/bionify_logo.png" alt="Bionify Logo" width="220"/>




  [![PyPI version](https://img.shields.io/pypi/v/bionify.svg)](https://pypi.org/project/bionify/)
  [![Python versions](https://img.shields.io/pypi/pyversions/bionify.svg)](https://pypi.org/project/bionify/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Pranay-Bhaskar/bionify)


  **Bionify** is a lightning-fast, C++ powered terminal formatter that applies Bionic Reading algorithms to your Python tracebacks and logs.

  By strategically bolding the first half of words, Bionify guides your eyes through massive walls of terminal text, allowing you to parse crash logs, errors, and system outputs in a fraction of the time.




  <p align="center">
    <img src="https://raw.githubusercontent.com/Pranay-Bhaskar/fovea/main/assets/demo.png" alt="Bionify Terminal Output Demo" width="400"/>
  </p>

</div>

## Features

- **Zero-Config Hooks:** Import it once, and Fovea automatically intercepts and styles your unhandled exceptions and `stderr` outputs.
- **Native Logging Integration:** Includes a custom formatter for Python's standard `logging` library.
- **Hyperlink Protection:** Smart enough to leave URLs (`https://`) and file paths (`C:\`) unformatted so they remain clickable in modern terminals like VS Code.
- **Blazing Fast Backend:** The text parsing engine is written entirely in C++ using `nanobind`, ensuring zero latency even on massive stack traces.
- **Custom Aesthetics:** Easily configure intensity, bolding, and ANSI colors to match your terminal theme.

## Installation

Currently available for Windows (64-bit).

```bash
pip install bionify
```

## Quick Start

The easiest way to use Fovea is to simply import it at the top of your entry-point file. It will automatically hook into `sys.excepthook` and `sys.stderr`.

```python
import bionify

# Bionify is now active! Any unhandled exceptions will be styled.
raise RuntimeError("This traceback will be styled for rapid reading!")
```

## Advanced Usage

### Customizing the Aesthetic

Fovea defaults to Bold Cyan with a 50% reading intensity. You can easily adjust this to match your terminal theme:

```python
import bionify

# Change the fixation intensity (0.1 to 1.0)
bionify.set_prescription(0.6)

# Change the color (cyan, magenta, yellow, red, green, blue, white)
bionify.set_style(bold=True, color="magenta")

# Power user? Pass your own raw ANSI escape sequences
bionify.set_color_ansi(prefix="\033[1;95m", suffix="\033[0m")
```

### Using with the logging Library

If you want to apply Bionify to your standard Python logs, use the provided `BionicFormatter`:

```python
import logging
from bionify.hook import BionicFormatter

logger = logging.getLogger("MyBackend")
handler = logging.StreamHandler()

# Attach the Fovea formatter
handler.setFormatter(BionicFormatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Database connection established successfully.")
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Pranay-Bhaskar/bionify/issues).

## License

This project is licensed under the [MIT License](LICENSE) © 2026 Pranay.