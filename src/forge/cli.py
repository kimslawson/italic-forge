"""Command line interface for italic-forge."""

from pathlib import Path
from typing import Annotated

import typer

from forge.font import FontInfo, FontReadError, read_font_info

app = typer.Typer(
    name="forge",
    help="Build and inspect OpenType fonts for future optical oblique workflows.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """Run italic-forge commands."""


def _format_optional_int(value: int | None) -> str:
    """Format optional integer font metadata for terminal output.

    Args:
        value: Integer value from a font table, or None when absent.

    Returns:
        A printable value.

    """
    return "not present" if value is None else str(value)


def _print_font_info(info: FontInfo) -> None:
    """Print font metadata in a stable, human-readable order.

    Args:
        info: Font metadata extracted from an OpenType file.

    """
    rows = [
        ("family", info.family),
        ("style", info.style),
        ("version", info.version),
        ("glyph count", str(info.glyph_count)),
        ("units per em", str(info.units_per_em)),
        ("ascender", str(info.ascender)),
        ("descender", str(info.descender)),
        ("x-height", _format_optional_int(info.x_height)),
        ("cap height", _format_optional_int(info.cap_height)),
        ("weight class", str(info.weight_class)),
        ("width class", str(info.width_class)),
        ("italic angle", f"{info.italic_angle:g}"),
    ]

    label_width = max(len(label) for label, _ in rows)
    for label, value in rows:
        typer.echo(f"{label:<{label_width}}  {value}")


@app.command()
def info(
    font: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            help="Path to an OpenType font file.",
        ),
    ],
) -> None:
    """Print OpenType metadata for a font."""
    try:
        font_info = read_font_info(font)
    except FontReadError as exc:
        raise typer.BadParameter(str(exc), param_hint="font") from exc

    _print_font_info(font_info)


if __name__ == "__main__":
    app()
