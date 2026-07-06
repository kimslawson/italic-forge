"""Metric helpers for font analysis and future generation steps."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VerticalMetrics:
    """Vertical metrics used by font analysis and export.

    Attributes:
        ascender: Typographic ascender.
        descender: Typographic descender.
        x_height: Optional x-height.
        cap_height: Optional cap height.

    """

    ascender: int
    descender: int
    x_height: int | None = None
    cap_height: int | None = None
