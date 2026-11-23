# === Stage 15: Слияние записей ===
# Project: ClimbLog
from typing import Any


def _pick(values: list, key: str, default: Any = None) -> Any:
    for v in values:
        if isinstance(v, dict) and key in v:
            return v[key]
    return default


def _first(values: list, index: int) -> Any:
    try:
        return values[index]
    except (IndexError, TypeError):
        return None


def merge_climb_records(
    records: list,
    keys: list,
    tiebreak: str = "first",
    default: Any = None,
) -> dict:
    """Merge two climb records by choosing a winner for each field.

    Args:
        records: a list containing two climb records to merge.
        keys: the field names to merge.
        tiebreak: "first" (default), "last", "non_empty", or "default".
        default: value used when no winner can be determined for a field.

    Returns:
        A new merged record dictionary.
    """
    if len(records) < 2:
        raise ValueError("merge_climb_records requires at least two records")

    first, second = records[0], records[1]
    merged: dict = {}

    for key in keys:
        first_val = _first(first, 0) if isinstance(first, list) else first.get(key)
        second_val = _first(second, 0) if isinstance(second, list) else second.get(key)

        if first_val is not None and second_val is not None:
            if tiebreak == "last":
                winner = second_val
            elif tiebreak == "non_empty":
                winner = second_val if second_val else first_val
            else:
                winner = first_val
        elif first_val is not None:
            winner = first_val
        elif second_val is not None:
            winner = second_val
        else:
            winner = default

        merged[key] = winner

    return merged
