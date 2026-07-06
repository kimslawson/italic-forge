"""Optical correction models for future italic and oblique generation."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OpticalProfile:
    """Describes intended optical behavior for a generated italic.

    Attributes:
        slant_angle_degrees: Target slant angle in degrees.
        preserve_stem_weight: Whether future transforms should compensate stem weight.

    """

    slant_angle_degrees: float
    preserve_stem_weight: bool = True
