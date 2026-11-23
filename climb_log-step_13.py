# === Stage 13: Быстрые фильтры ===
# Project: ClimbLog
from datetime import datetime, timedelta


def _today() -> datetime:
    return datetime.now()


def _start_of_week(today: datetime) -> datetime:
    monday = today - timedelta(days=today.weekday())
    return monday.replace(hour=0, minute=0, second=0, microsecond=0)


def is_climbed_today(climb_date: datetime) -> bool:
    return climb_date.date() == _today().date()


def is_climbed_this_week(climb_date: datetime, week_start: datetime | None = None) -> bool:
    if week_start is None:
        week_start = _start_of_week(_today())
    return week_start <= climb_date < week_start + timedelta(days=7)


def is_overdue(climb_date: datetime, due_date: datetime) -> bool:
    return climb_date < due_date and _today().date() >= due_date.date()


def filter_climbs_by_date(climbs: list[dict], climb_date: datetime) -> bool:
    return is_climbed_today(climb_date) or is_climbed_this_week(climb_date)


def filter_overdue_climbs(climbs: list[dict], due_date: datetime) -> bool:
    return is_overdue(climbs.get("climb_date", datetime.min.replace(year=2000)), due_date)
