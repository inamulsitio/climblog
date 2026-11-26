# === Stage 21: Просмотр истории ===
# Project: ClimbLog
from datetime import date


def format_climb(
    name: str,
    category: str,
    length: float,
    ascent_date: date,
) -> str:
    """Return a compact one-line history view of a single climb record."""
    length_str = f"{length:g} m"
    date_str = ascent_date.isoformat()
    return f"{name} | {category} | {length_str} | {date_str}"


if __name__ == "__main__":
    sample = format_climb(
        name="The Nose",
        category="5.10a",
        length=305.0,
        ascent_date=date(2024, 6, 14),
    )
    print(sample)
