# === Stage 7: Фильтрация записей ===
# Project: ClimbLog
from datetime import date


def filter_by_category(courses, category):
    return [c for c in courses if c["category"] == category]


def filter_by_date_range(courses, start_date, end_date):
    return [c for c in courses if start_date <= c["date"] <= end_date]


def filter_courses(courses, category=None, start_date=None, end_date=None):
    result = courses
    if category is not None:
        result = filter_by_category(result, category)
    if start_date is not None:
        result = filter_by_date_range(result, start_date, end_date)
    return result
