# === Stage 14: Поиск дубликатов ===
# Project: ClimbLog
from datetime import date


def normalize_name(name):
    return " ".join(name.strip().lower().split())


def normalize_category(category):
    return category.strip().lower()


def normalize_length(length):
    return float(length)


def normalize_date(day, month, year):
    try:
        return date(year, month, day)
    except (ValueError, TypeError):
        return None


def normalize_route(route):
    return (
        normalize_name(route.get("name")),
        normalize_category(route.get("category")),
        normalize_length(route.get("length")),
        normalize_date(route.get("day"), route.get("month"), route.get("year")),
    )


def find_duplicate_routes(routes):
    seen = {}
    duplicates = []
    for route in routes:
        key = normalize_route(route)
        if key is not None and key in seen:
            duplicates.append((seen[key], route))
        else:
            seen[key] = route
    return duplicates
