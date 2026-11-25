# === Stage 17: Избранное ===
# Project: ClimbLog
import datetime

class Route:
    def __init__(self, name, grade, length, date):
        self.name = name
        self.grade = grade
        self.length = length
        self.date = date
        self.is_favorite = False

    def toggle_favorite(self):
        self.is_favorite = not self.is_favorite

    def __repr__(self):
        favorite = "★" if self.is_favorite else " "
        return f"{favorite} {self.name} ({self.grade}, {self.length}m)"


class ClimbLog:
    def __init__(self):
        self.routes = []

    def add_route(self, name, grade, length, date):
        self.routes.append(Route(name, grade, length, date))

    def get_favorite_routes(self):
        return [route for route in self.routes if route.is_favorite]

    def toggle_favorite(self, route):
        route.toggle_favorite()
