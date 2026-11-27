# === Stage 25: Серии по дням ===
# Project: ClimbLog
from collections import OrderedDict


def find_streaks(records):
    """Return a list of consecutive-day streaks.

    Each streak is a list of records sorted by date. A streak is a maximal
    run of records whose dates are each exactly one day after the previous.
    """
    if not records:
        return []

    ordered = sorted(records, key=lambda r: r["date"])

    streaks = []
    current = [ordered[0]]

    for previous, current_record in zip(ordered, ordered[1:]):
        if (current_record["date"] - previous["date"]).days == 1:
            current.append(current_record)
        else:
            streaks.append(current)
            current = [current_record]

    streaks.append(current)
    return streaks


def longest_streak_days(records):
    """Return the number of days in the longest consecutive-day streak."""
    streaks = find_streaks(records)
    return max(len(streak) for streak in streaks)


def streak_of_days(start_date, end_date):
    """Return the number of days between two dates, inclusive."""
    return (end_date - start_date).days + 1


def streak_summary(records):
    """Return a compact summary of the longest streak.

    The summary is a list of (start_date, end_date, length) tuples.
    """
    streaks = find_streaks(records)
    best = max(streaks, key=len, default=[])
    if not best:
        return []

    best_sorted = sorted(best, key=lambda r: r["date"])
    start_date = best_sorted[0]["date"]
    end_date = best_sorted[-1]["date"]
    return [(start_date, end_date, len(best_sorted))]
