"""OpenType font loading and metadata extraction."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from fontTools.ttLib import TTFont, TTLibError


class FontReadError(RuntimeError):
    """Raised when a font cannot be read or lacks required tables."""


@dataclass(frozen=True, slots=True)
class FontInfo:
    """Metadata reported by the ``forge info`` command.

    Attributes:
        family: Preferred family name, falling back to legacy family records.
        style: Preferred style name, falling back to subfamily records.
        version: Version string from the name table.
        glyph_count: Number of glyphs in the font.
        units_per_em: Units per em from the head table.
        ascender: Typographic ascender.
        descender: Typographic descender.
        x_height: x-height from the OS/2 table, when present.
        cap_height: Cap height from the OS/2 table, when present.
        weight_class: OpenType weight class.
        width_class: OpenType width class.
        italic_angle: Italic angle from the post table.

    """

    family: str
    style: str
    version: str
    glyph_count: int
    units_per_em: int
    ascender: int
    descender: int
    x_height: int | None
    cap_height: int | None
    weight_class: int
    width_class: int
    italic_angle: float


def read_font_info(path: Path) -> FontInfo:
    """Read high-level metadata from an OpenType font.

    Args:
        path: Path to a TrueType or OpenType font.

    Returns:
        Metadata suitable for display in the CLI.

    Raises:
        FontReadError: If the font cannot be opened or required tables are missing.

    """
    try:
        with TTFont(path, lazy=True) as font:
            return _extract_font_info(font)
    except (OSError, TTLibError, KeyError, AttributeError) as exc:
        raise FontReadError(f"Unable to read OpenType metadata from {path}") from exc


def _extract_font_info(font: TTFont) -> FontInfo:
    """Extract reportable font metadata from an opened font.

    Args:
        font: Open fontTools font object.

    Returns:
        A populated font metadata object.

    """
    name_table = font["name"]
    head_table = font["head"]
    horizontal_header = font["hhea"]
    os2_table = font["OS/2"]
    post_table = font["post"]

    return FontInfo(
        family=_best_name(name_table, preferred_ids=(16, 1), default="Unknown"),
        style=_best_name(name_table, preferred_ids=(17, 2), default="Regular"),
        version=_best_name(name_table, preferred_ids=(5,), default="Unknown"),
        glyph_count=len(font.getGlyphOrder()),
        units_per_em=int(head_table.unitsPerEm),
        ascender=int(getattr(os2_table, "sTypoAscender", horizontal_header.ascent)),
        descender=int(getattr(os2_table, "sTypoDescender", horizontal_header.descent)),
        x_height=_optional_int_attr(os2_table, "sxHeight"),
        cap_height=_optional_int_attr(os2_table, "sCapHeight"),
        weight_class=int(os2_table.usWeightClass),
        width_class=int(os2_table.usWidthClass),
        italic_angle=float(post_table.italicAngle),
    )


def _best_name(name_table: Any, *, preferred_ids: tuple[int, ...], default: str) -> str:
    """Return the best Unicode name record for a list of OpenType name IDs.

    Args:
        name_table: A fontTools name table.
        preferred_ids: Name IDs in priority order.
        default: Value to return when no usable name is present.

    Returns:
        A decoded name string.

    """
    for name_id in preferred_ids:
        value = str(name_table.getDebugName(name_id) or "").strip()
        if value:
            return value
    return default


def _optional_int_attr(table: Any, attr: str) -> int | None:
    """Read an optional integer attribute from a fontTools table.

    Args:
        table: Font table object.
        attr: Attribute name to read.

    Returns:
        The integer value when present, otherwise None.

    """
    value = getattr(table, attr, None)
    return None if value is None else int(value)
