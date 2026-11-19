# === Stage 4: Редактирование записей ===
# Project: ClimbLog
ALLOWED_ROUTE_FIELDS = ("name", "grade", "length", "date")


def update_route(route_id, updates, routes):
    """Edit an existing route by id, touching only allowed fields.

    Returns the updated route dict on success or None if the route is
    missing or ``updates`` is empty or contains disallowed keys.
    """
    if not updates:
        return None

    route = next((r for r in routes if r["id"] == route_id), None)
    if route is None:
        return None

    for key in updates:
        if key not in ALLOWED_ROUTE_FIELDS:
            return None

    for key, value in updates.items():
        route[key] = value

    return route


def validate_route(route):
    """Return True if ``route`` has all required fields, correct types
    and a non-empty name.
    """
    if not isinstance(route, dict):
        return False

    required = ("id", "name", "grade", "length", "date")
    for field in required:
        if field not in route:
            return False

    if not isinstance(route["name"], str) or not route["name"].strip():
        return False

    if not isinstance(route["grade"], str) or not route["grade"].strip():
        return False

    if not isinstance(route["length"], (int, float)) or route["length"] <= 0:
        return False

    if not isinstance(route["date"], str) or not route["date"].strip():
        return False

    return True
