# === Stage 23: Месячный отчёт ===
# Project: ClimbLog
from datetime import datetime, timedelta


def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()


def format_date(value):
    return value.strftime("%Y-%m-%d")


def month_name(year, month):
    return datetime(year, month, 1).strftime("%B %Y")


def group_by_month(records):
    grouped = {}
    for record in records:
        key = record["date"][:7]
        grouped.setdefault(key, []).append(record)
    return grouped


def monthly_totals(records):
    grouped = group_by_month(records)
    totals = {}
    for key in sorted(grouped):
        attempts = grouped[key]
        totals[key] = {
            "attempts": len(attempts),
            "first_time": sum(
                1 for rec in attempts if rec.get("first_time", False)
            ),
            "new_routes": sum(
                1 for rec in attempts if rec.get("new_route", False)
            ),
            "failed": sum(1 for rec in attempts if not rec.get("succeeded", False)),
        }
    return totals


def previous_month(year, month):
    if month == 1:
        return year - 1, 12
    return year, month - 1


def month_comparison(totals, year, month):
    current = totals.get(f"{year:02d}{month:02d}", {})
    prev_year, prev_month = previous_month(year, month)
    previous = totals.get(f"{prev_year:02d}{prev_month:02d}", {})
    return {
        "current": current,
        "previous": previous,
        "delta": {
            "attempts": current.get("attempts", 0) - previous.get("attempts", 0),
            "first_time": current.get("first_time", 0) - previous.get("first_time", 0),
            "new_routes": current.get("new_routes", 0) - previous.get("new_routes", 0),
            "failed": current.get("failed", 0) - previous.get("failed", 0),
        },
    }


def monthly_report(records, year, month):
    totals = monthly_totals(records)
    comparison = month_comparison(totals, year, month)
    name = month_name(year, month)
    stats = comparison["current"]
    return {
        "name": name,
        "attempts": stats.get("attempts", 0),
        "first_time": stats.get("first_time", 0),
        "new_routes": stats.get("new_routes", 0),
        "failed": stats.get("failed", 0),
        "success_rate": (
            round(
                (stats.get("attempts", 0) - stats.get("failed", 0))
                / stats.get("attempts", 1) * 100, 1
            )
            if stats.get("attempts", 0)
            else 0.0
        ),
        "delta": comparison["delta"],
    }
