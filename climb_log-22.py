# === Stage 22: Недельный отчёт ===
# Project: ClimbLog
from datetime import datetime

def format_date(value):
    if value is None:
        return "n/a"
    try:
        return value.strftime("%Y-%m-%d")
    except AttributeError:
        return str(value)

def weekly_report(climbs, start, end):
    if start is None or end is None:
        start = datetime.now()
        end = datetime.now()
    start = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = end.replace(hour=23, minute=59, second=59, microsecond=0)
    rows = [c for c in climbs if start <= c.get("date", datetime.min) <= end]
    total_attempts = sum(r["attempts"] for r in rows)
    total_successes = sum(r["successes"] for r in rows)
    total_distance = sum(r["length"] * r["attempts"] for r in rows)
    lines = []
    lines.append("Climb Log Weekly Report")
    lines.append("=" * 60)
    lines.append(f"From: {format_date(start)}  To: {format_date(end)}")
    lines.append("-" * 60)
    lines.append(f"{'#':>3}  {'Route':<20} {'Grade':<8} {'Len':>5}  {'Att':>4}  {'OK':>4}")
    lines.append("-" * 60)
    for i, r in enumerate(rows, 1):
        lines.append(f"{i:>3}  {r.get('name', 'n/a'):<20} {r.get('grade', 'n/a'):<8} "
                     f"{r.get('length', 0):>5.1f}  {r.get('attempts', 0):>4}  {r.get('successes', 0):>4}")
    lines.append("-" * 60)
    lines.append(f"Total routes: {len(rows)}")
    lines.append(f"Total attempts: {total_attempts}")
    lines.append(f"Total successes: {total_successes}")
    if total_attempts:
        lines.append(f"Success rate: {total_successes / total_attempts * 100:.1f}%")
    else:
        lines.append("Success rate: n/a")
    lines.append(f"Total distance: {total_distance:.1f} m")
    return "\n".join(lines)
