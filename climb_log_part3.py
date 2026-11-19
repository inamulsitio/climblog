# === Stage 3: Хранилище в памяти ===
# Project: ClimbLog
from uuid import uuid4

Route = dict


class RouteStore:
    def __init__(self):
        self._routes = {}

    def add(self, name, grade, length, when):
        route = {
            "id": str(uuid4()),
            "name": name,
            "grade": grade,
            "length": length,
            "when": when,
        }
        self._routes[route["id"]] = route
        return route

    def get(self, route_id):
        return self._routes.get(route_id)

    def list(self):
        return list(self._routes.values())
