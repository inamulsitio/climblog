# === Stage 1: Каркас модуля ===
# Project: ClimbLog
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Route:
    name: str
    grade: str
    length: float
    date: date


def make_demo_routes() -> list[Route]:
    return [
        Route("North Face", "5.10a", 12.5, date(2023, 5, 14)),
        Route("The Crux", "5.12b", 18.0, date(2023, 6, 2)),
        Route("Sunlit Gully", "5.8", 9.2, date(2023, 7, 21)),
    ]


def main() -> None:
    routes = make_demo_routes()
    for route in routes:
        print(f"{route.name} | {route.grade} | {route.length} m | {route.date}")


if __name__ == "__main__":
    main()
