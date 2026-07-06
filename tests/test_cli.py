from pathlib import Path

from typer.testing import CliRunner

from forge.cli import app

EXAMPLE_FONT = Path("examples/bricolage/input/BricolageGrotesque-Regular.ttf")


def test_info_command_prints_font_metadata() -> None:
    result = CliRunner().invoke(app, ["info", str(EXAMPLE_FONT)])

    assert result.exit_code == 0
    assert "family" in result.output
    assert "Bricolage Grotesque" in result.output
    assert "glyph count" in result.output
    assert "italic angle" in result.output
