# === Stage 16: Массовое обновление ===
# Project: ClimbLog
from typing import List, Callable, Dict, Any, Tuple

Route = Dict[str, Any]
RouteId = str
Change = Tuple[RouteId, str, Any, Any]


def preview_changes(routes: List[Route],
                    condition: Callable[[Route], bool],
                    updater: Callable[[Route], Any]) -> List[Change]:
    return [(rid, rid, None, updater(route))
            for rid, route in routes.items()
            if condition(route)]


def apply_changes(routes: Dict[RouteId, Route],
                  changes: List[Change]) -> None:
    for rid, old, new, value in changes:
        routes[rid][new] = value
