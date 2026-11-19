# === Stage 5: Удаление и восстановление ===
# Project: ClimbLog
from __future__ import annotations


class Route:
    """A climbing route with metadata and a collection of attempts."""

    def __init__(self, name, category, length, date) -> None:
        self.name = name
        self.category = category
        self.length = length
        self.date = date
        self.attempts: list[dict] = []

    def add_attempt(self, attempt: dict) -> None:
        self.attempts.append(attempt)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "category": self.category,
            "length": self.length,
            "date": self.date,
            "attempts": self.attempts,
            "_soft_deleted": False,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Route":
        route = cls(
            data["name"],
            data["category"],
            data["length"],
            data["date"],
        )
        route.attempts = list(data.get("attempts", []))
        route._soft_deleted = data.get("_soft_deleted", False)
        return route

    def soft_delete(self) -> None:
        self._soft_deleted = True

    def restore(self) -> None:
        self._soft_deleted = False

    def is_deleted(self) -> bool:
        return self._soft_deleted

    def hard_delete(self) -> None:
        self._soft_deleted = True
        self.attempts = []
        self.name = ""
        self.category = ""
        self.length = None
        self.date = None
