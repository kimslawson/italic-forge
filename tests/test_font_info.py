from pathlib import Path

from forge.font import read_font_info

EXAMPLE_FONT = Path("examples/bricolage/input/BricolageGrotesque-Regular.ttf")
EXPECTED_UNITS_PER_EM = 1000
EXPECTED_REGULAR_WEIGHT = 400
EXPECTED_NORMAL_WIDTH = 5


def test_read_font_info_extracts_expected_metadata() -> None:
    info = read_font_info(EXAMPLE_FONT)

    assert info.family == "Bricolage Grotesque"
    assert info.style == "Regular"
    assert info.glyph_count > 0
    assert info.units_per_em == EXPECTED_UNITS_PER_EM
    assert info.weight_class == EXPECTED_REGULAR_WEIGHT
    assert info.width_class == EXPECTED_NORMAL_WIDTH
    assert info.italic_angle == 0


def test_read_font_info_reports_optional_vertical_metrics() -> None:
    info = read_font_info(EXAMPLE_FONT)

    assert info.x_height is None or isinstance(info.x_height, int)
    assert info.cap_height is None or isinstance(info.cap_height, int)
