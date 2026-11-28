# === Stage 26: Топ записей ===
# Project: ClimbLog
# climblog_top.py
# Standalone module: top-N climbing routes by a chosen metric.
# Pure standard library, no external references.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, TypeVar, Callable


Route = TypeVar("Route")


@dataclass
class Record:
    """A single route record with a primary metric and optional metadata."""

    name: str
    metric: float
    length: float = 0.0
    date: str = ""
    extra: dict = field(default_factory=dict)


def sort_key(metric: Callable[[Route], float]) -> Callable[[Route], float]:
    """Return a key function that sorts routes by the given metric."""

    def key(record: Route) -> float:
        return metric(record)

    return key


def top_n(
    records: Iterable[Route],
    metric: Callable[[Route], float],
    n: int,
    *,
    reverse: bool = False,
) -> list[Route]:
    """Return the top-N records for the given metric.

    Args:
        records: an iterable of route records.
        metric: a callable mapping a record to a comparable value.
        n: how many records to return.
        reverse: when True, return the lowest-valued records instead.
    """

    n = max(0, n)
    if n == 0:
        return []

    items = sorted(records, key=sort_key(metric), reverse=reverse)
    return items[:n]


def find_top_difficulties(
    records: Iterable[Record],
    n: int = 5,
) -> list[Record]:
    """Return the hardest routes, ranked by difficulty score."""

    return top_n(records, metric=lambda r: r.metric, n=n, reverse=True)


def find_shortest(
    records: Iterable[Record],
    n: int = 5,
) -> list[Record]:
    """Return the shortest routes, ranked by length."""

    return top_n(records, metric=lambda r: r.length, n=n, reverse=False)


def find_newest(
    records: Iterable[Record],
    n: int = 5,
) -> list[Record]:
    """Return the most recently climbed routes, ranked by date."""

    return top_n(
        records,
        metric=lambda r: r.date,
        n=n,
        reverse=True,
    )


def find_most_climbed(
    records: Iterable[Record],
    n: int = 5,
) -> list[Record]:
    """Return the most frequently attempted routes."""

    counts: dict[str, int] = {}
    for record in records:
        counts[record.name] = counts.get(record.name, 0) + 1

    scored: list[tuple[str, int]] = list(counts.items())
    return top_n(scored, metric=lambda item: item[1], n=n, reverse=True)


if __name__ == "__main__":
    sample = [
        Record("A1", 12.0, 15.0, "2023-01-05"),
        Record("B2", 15.5, 20.0, "2023-02-10"),
        Record("C3", 9.0, 12.0, "2023-03-20"),
        Record("D4", 18.0, 25.0, "2023-04-01"),
    ]

    print("Hardest routes:")
    for route in find_top_difficulties(sample, n=3):
        print(f"  {route.name}  difficulty={route.metric}")

    print("Shortest routes:")
    for route in find_shortest(sample, n=2):
        print(f"  {route.name}  length={route.length}")

    print("Most climbed routes:")
    for route in find_most_climbed(sample, n=2):
        print(f"  {route.name}  attempts={route.extra.get('attempts', 0)}")
