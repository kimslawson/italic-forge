# italic-forge

italic-forge is an early-stage Python toolkit for generating high-quality optical obliques
and semi-automatic italics from OpenType fonts.

The project currently focuses on a clean foundation: typed font inspection, a Typer CLI,
modern packaging, tests, and room for future geometry and optical correction systems.
Italic generation is intentionally not implemented yet.

## Requirements

- Python 3.14+
- uv

## Install for development

```bash
uv sync
```

## CLI

Inspect an OpenType font:

```bash
uv run forge info examples/bricolage/input/BricolageGrotesque-Regular.ttf
```

The command prints:

- family
- style
- version
- glyph count
- units per em
- ascender
- descender
- x-height, when present
- cap height, when present
- weight class
- width class
- italic angle

## Development

```bash
make check
```

This runs Ruff, mypy, and pytest.

## Project Layout

```text
src/
    forge/
        cli.py       # Typer command line interface
        config.py    # Shared configuration dataclasses
        font.py      # OpenType loading and metadata extraction
        geometry.py  # Future geometric transforms
        optics.py    # Future optical correction model
        metrics.py   # Font metric helpers
        naming.py    # Font naming helpers
        export.py    # Future export pipeline
```

## Status

Pre-alpha. Public APIs may change while the italic generation pipeline is designed.
