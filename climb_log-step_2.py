# === Stage 2: Проверка полей ===
# Project: ClimbLog
"""ClimbLog - route field validation and input normalization module."""

import datetime


def normalize_text(value):
    """Return a trimmed, title-cased string, or None if input is blank."""
    if value is None:
        return None
    text = str(value).strip()
    return text.title() if text else None


def normalize_category(value):
    """Return a trimmed, lower-cased category string, or None if blank."""
    if value is None:
        return None
    text = str(value).strip()
    return text.lower() if text else None


def normalize_length(value):
    """Return a positive float length in meters, or None if invalid."""
    if value is None:
        return None
    try:
        length = float(value)
    except (TypeError, ValueError):
        return None
    if length <= 0:
        return None
    return round(length, 2)


def normalize_date(value):
    """Parse a date string into a datetime.date, or None if invalid."""
    if value is None:
        return None
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            parsed = datetime.datetime.strptime(text, fmt).date()
            return parsed
        except ValueError:
            continue
    return None


def validate_route(name, category, length, date):
    """Validate a route entity.

    Returns a tuple (is_valid, errors) where errors is a list of
    human-readable messages for the fields that failed validation.
    """
    errors = []

    normalized_name = normalize_text(name)
    if normalized_name is None:
        errors.append("Название маршрута обязательно.")
    else:
        if len(normalized_name) < 2:
            errors.append("Название маршрута слишком короткое.")

    normalized_category = normalize_category(category)
    if normalized_category is None:
        errors.append("Категория обязательна.")
    elif normalized_category not in (
        "trad", "sport", "aid", "boulder", "toprope", "lead", "roof", "crack"
    ):
        errors.append("Неизвестная категория маршрута.")

    normalized_length = normalize_length(length)
    if normalized_length is None:
        errors.append("Укажите длину маршрута в метрах.")
    else:
        if normalized_length > 400:
            errors.append("Длина маршрута превышает разумные пределы.")

    normalized_date = normalize_date(date)
    if normalized_date is None:
        errors.append("Укажите дату в формате ГГГГ-ММ-ДД.")
    else:
        today = datetime.date.today()
        if normalized_date > today:
            errors.append("Дата не может быть в будущем.")

    return (len(errors) == 0, errors)
