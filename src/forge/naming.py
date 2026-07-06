"""Font naming helpers for future generated families."""


def build_style_name(base_style: str, suffix: str) -> str:
    """Build a derived style name.

    Args:
        base_style: Existing style name.
        suffix: Style suffix such as ``Oblique`` or ``Italic``.

    Returns:
        A normalized derived style name.

    """
    normalized_base = base_style.strip()
    normalized_suffix = suffix.strip()
    if not normalized_base:
        return normalized_suffix
    if not normalized_suffix:
        return normalized_base
    return f"{normalized_base} {normalized_suffix}"
