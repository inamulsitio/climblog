# === Stage 6: Связанная сущность ===
# Project: ClimbLog
from datetime import date

class Attempt:
    __id_counter = 1
    def __init__(self, route_id, date, grade, holds, crux, notes):
        self.id = Attempt.__id_counter
        Attempt.__id_counter += 1
        self.route_id = route_id
        self.date = date
        self.grade = grade
        self.holds = holds
        self.crux = crux
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "route_id": self.route_id,
            "date": self.date,
            "grade": self.grade,
            "holds": self.holds,
            "crux": self.crux,
            "notes": self.notes,
        }

    def is_redpoint(self):
        return self.crux == "redpoint"

    def is_flash(self):
        return self.crux == "flash"

    def is_on_sight(self):
        return self.crux == "onsight"

    def is_topout(self):
        return self.crux == "topout"

    def is_failed(self):
        return self.crux == "failed"

    def days_since(self, today=None):
        if today is None:
            today = date.today()
        delta = today - self.date
        return delta.days

    def __repr__(self):
        return "Attempt(id={id}, route_id={route_id}, date={date}, grade={grade}, crux={crux})".format(
            id=self.id, route_id=self.route_id, date=self.date, grade=self.grade, crux=self.crux
        )
