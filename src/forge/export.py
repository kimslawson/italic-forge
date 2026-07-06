"""Export pipeline boundaries for future generated fonts."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ExportPlan:
    """Describes where a future generated font should be written.

    Attributes:
        output_path: Destination path for the generated font.
        overwrite: Whether an existing output file may be replaced.

    """

    output_path: Path
    overwrite: bool = False
