# === Stage 19: Смена статуса ===
# Project: ClimbLog
from enum import Enum


class RouteStatus(Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    ABANDONED = "abandoned"


_TRANSITIONS = {
    RouteStatus.PLANNED: {RouteStatus.IN_PROGRESS, RouteStatus.ABANDONED},
    RouteStatus.IN_PROGRESS: {RouteStatus.DONE, RouteStatus.ABANDONED},
    RouteStatus.DONE: set(),
    RouteStatus.ABANDONED: set(),
}


class Route:
    def __init__(self, name, category, length, date):
        self.name = name
        self.category = category
        self.length = length
        self.date = date
        self.status = RouteStatus.PLANNED

    def change_status(self, new_status, reason):
        if new_status not in _TRANSITIONS[self.status]:
            raise ValueError(
                f"Invalid transition from {self.status.value} to {new_status.value}"
            )
        if not reason:
            raise ValueError("Reason cannot be empty")
        self.status = new_status
        self.status_reason = reason

    def __repr__(self):
        return (
            f"Route(name={self.name!r}, category={self.category!r}, "
            f"length={self.length!r}, date={self.date!r}, "
            f"status={self.status.value!r}, reason={self.status_reason!r})"
        )
