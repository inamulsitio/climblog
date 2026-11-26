# === Stage 20: История изменений ===
# Project: ClimbLog
from datetime import datetime


class RouteChange:
    """Records a single modification to a route."""

    def __init__(self, field, old_value, new_value, note=""):
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.note = note
        self.date = datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        return {
            "date": self.date,
            "field": self.field,
            "old_value": self.old_value,
            "new_value": self.new_value,
            "note": self.note,
        }

    def __repr__(self):
        return (
            f"RouteChange(field={self.field!r}, "
            f"old={self.old_value!r}, new={self.new_value!r}, "
            f"date={self.date!r})"
        )


class RouteHistory:
    """Keeps the chronological list of changes for a route."""

    def __init__(self):
        self.changes = []

    def add(self, field, old_value, new_value, note=""):
        self.changes.append(
            RouteChange(field, old_value, new_value, note)
        )

    def latest(self):
        return self.changes[-1] if self.changes else None

    def summary(self):
        return [c.to_dict() for c in reversed(self.changes)]

    def __len__(self):
        return len(self.changes)

    def __repr__(self):
        return f"RouteHistory(changes={len(self.changes)})"
