# Python Data Filter

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ci](https://github.com/Jayllyz/py-data-filter/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/Jayllyz/py-data-filter/actions/workflows/ci.yaml)

## Setup development environment

Requirements:

- Python 3.8+
- [uv](https://github.com/astral-sh/uv)

```bash
# Install dependencies
uv pip install -r requirements.txt

# Generate requirements.txt
uv pip freeze | uv pip compile - -o requirements.txt --python-platform=linux
```

## Ruff commands

Recommended to use [ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) in VSCode.

```bash
ruff check --fix # Lint and fix code
ruff format # Format code
```
