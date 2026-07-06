"""Configuration models for italic-forge workflows."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ForgeConfig:
    """Global configuration for future font generation workflows.

    Attributes:
        preserve_overlaps: Whether outline overlaps should be preserved during export.

    """

    preserve_overlaps: bool = True
