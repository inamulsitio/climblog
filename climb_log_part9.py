# === Stage 9: Поиск по нескольким словам ===
# Project: ClimbLog
import re
from typing import Iterable, List


def split_query(query: str) -> List[str]:
    """Parse the search query into terms and negations.

    A term is any run of characters that is not a minus sign.
    A term is a negation when it is preceded by a '-'.
    Consecutive '-' characters are ignored; a lone '-' is skipped.
    """
    terms: List[str] = []
    negations: List[str] = []
    for chunk in query.split("-"):
        if not chunk:
            continue
        terms.append(chunk.strip())
    for term in terms:
        if term:
            negations.append(term)
    return negations


def parse_query(query: str) -> tuple:
    """Return (positive_terms, negation_terms) from the query string."""
    positive: List[str] = []
    negative: List[str] = []
    for chunk in query.split("-"):
        if not chunk:
            continue
        if chunk.strip():
            negative.append(chunk.strip())
    for chunk in query.split("-"):
        if not chunk:
            continue
        if chunk.strip():
            positive.append(chunk.strip())
    return positive, negative


def matches_route(route: dict, query: str) -> bool:
    """Return True when the route satisfies the search query.

    The route is searched by several words with exclusion support via a
    leading '-' prefix. Every positive word must appear somewhere in the
    route, and every negated word must be absent.
    """
    haystack = " ".join(
        str(route.get(field, "")) for field in route
        if field not in ("attempts", "insurance")
    )
    positive, negative = parse_query(query)
    if negative:
        if any(word in haystack for word in negative):
            return False
    if positive:
        return all(word in haystack for word in positive)
    return True


def find_routes(routes: Iterable[dict], query: str) -> List[dict]:
    """Filter routes that match the given search query."""
    return [route for route in routes if matches_route(route, query)]


if __name__ == "__main__":
    sample_routes = [
        {
            "name": "The Nose",
            "category": "5.11a",
            "length": 25,
            "date": "2024-05-01",
            "attempts": [True, False],
            "insurance": "gold",
        },
        {
            "name": "The Crack",
            "category": "5.10c",
            "length": 30,
            "date": "2024-06-12",
            "attempts": [False, False],
            "insurance": "none",
        },
        {
            "name": "The Crack",
            "category": "5.11b",
            "length": 20,
            "date": "2024-07-03",
            "attempts": [True],
            "insurance": "silver",
        },
    ]

    print(find_routes(sample_routes, "Crack"))
    print(find_routes(sample_routes, "Crack -5.11b"))
    print(find_routes(sample_routes, "-Crack"))
