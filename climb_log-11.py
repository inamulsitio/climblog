# === Stage 11: Группировка ===
# Project: ClimbLog
from collections import Counter


def group_routes_by_category(routes):
    """Group routes by their category and count entries in each group.

    Args:
        routes: An iterable of route records. Each record is a mapping-like
            object exposing a ``category`` attribute or key.

    Returns:
        A Counter mapping each distinct category to the number of routes that
        share it. Categories that appear on zero routes are omitted.
    """
    counts = Counter()
    for route in routes:
        category = route.get("category")
        if category is None:
            continue
        counts[category] += 1
    return counts


def top_categories_by_count(categorized_counts, limit):
    """Return the ``limit`` categories with the most routes.

    Ties are broken by category name so the ordering is stable and
    reproducible across runs.

    Args:
        categorized_counts: A mapping from category to its route count.
        limit: The maximum number of categories to return.

    Returns:
        A list of ``(category, count)`` tuples sorted by descending count and
        then ascending category name.
    """
    ordered = sorted(categorized_counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:limit]


def summarize_climb_session(routes):
    """Produce a compact summary of a climbing session.

    Args:
        routes: An iterable of route records with a ``category`` field.

    Returns:
        A tuple ``(total, by_category)`` where ``total`` is the number of
        routes and ``by_category`` is a Counter of category to count.
    """
    by_category = Counter()
    for route in routes:
        category = route.get("category")
        if category is not None:
            by_category[category] += 1
    return len(routes), by_category


if __name__ == "__main__":
    sample = [
        {"name": "Pine Needles", "category": "5.10a", "length": 18, "grade": "S"},
        {"name": "The Nose", "category": "5.11c", "length": 24, "grade": "H"},
        {"name": "Sloper", "category": "5.10a", "length": 12, "grade": "S"},
        {"name": "Crux", "category": "5.12a", "length": 20, "grade": "H"},
    ]
    grouped = group_routes_by_category(sample)
    for category, count in top_categories_by_count(grouped, 3):
        print(f"{category}: {count}")
