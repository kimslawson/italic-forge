"""Geometry primitives for future outline transformations."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Shear:
    """A simple shear transform descriptor.

    Attributes:
        angle_degrees: Shear angle in degrees.
        pivot_y: Vertical pivot position in font units.

    """

    angle_degrees: float
    pivot_y: float = 0.0
