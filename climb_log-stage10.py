# === Stage 10: Теги ===
# Project: ClimbLog
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set


@dataclass
class Route:
    name: str
    grade: str
    length: float
    date: str
    tags: Set[str] = field(default_factory=set)


class TagManager:
    def __init__(self) -> None:
        self._route_tags: Dict[str, Set[str]] = {}

    def add_tag(self, route: Route, tag: str) -> None:
        if not tag or not route:
            return
        self._route_tags.setdefault(route, set()).add(tag)

    def remove_tag(self, route: Route, tag: str) -> None:
        if route in self._route_tags:
            self._route_tags[route].discard(tag)
            if not self._route_tags[route]:
                del self._route_tags[route]

    def search_by_tag(self, tag: str) -> List[Route]:
        return [route for route, tags in self._route_tags.items() if tag in tags]
