# === Stage 24: Скользящее среднее ===
# Project: ClimbLog
from collections import Counter


def moving_average(values, window):
    """Return a list of trailing moving averages over ``window`` samples.

    ``values`` is an iterable of numbers. Each output element is the mean of
    the last ``window`` numbers ending at the current position. The first
    ``window - 1`` positions have too few samples to form a full window and
    are skipped, matching the common convention used in climb statistics.
    """
    if window <= 0:
        raise ValueError("window must be a positive integer")

    counts = Counter()
    running_sum = 0.0
    averages = []

    for value in values:
        counts[value] += 1
        running_sum += value
        if counts[value] == window:
            averages.append(running_sum / window)
        else:
            averages.append(None)

    return averages


def moving_average_by_route(route_id, values, window):
    """Compute a moving average for a single climb route.

    ``route_id`` identifies a route entity, ``values`` are the numeric
    measurements recorded for that route (for example the average hold
    grade or the number of falls), and ``window`` is the number of recent
    attempts to include in each average. Returns a list aligned with
    ``values`` where early entries are ``None`` until a full window exists.
    """
    return moving_average(values, window)


def smooth_route_metric(route_id, values, window):
    """Smooth a numeric route metric to reduce noise from single attempts.

    This helper wraps :func:`moving_average_by_route` so callers can pass a
    route identifier together with its historical measurements and obtain a
    stabilized value that is less sensitive to one unusually hard or easy
    attempt. Useful when displaying a route's typical difficulty or fall
    rate in the journal UI.
    """
    return moving_average_by_route(route_id, values, window)


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value, average in zip(sample, moving_average(sample, 3)):
        print(value, "->", average)
