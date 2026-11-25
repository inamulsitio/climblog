# === Stage 18: Статусы записей ===
# Project: ClimbLog
from enum import Enum, auto


class RouteLifecycle(Enum):
    DISCOVERED = auto()
    PLANNED = auto()
    REHEARSED = auto()
    ATTEMPTED = auto()
    SUCCEEDED = auto()
    GAVE_UP = auto()


_TRANSITIONS = {
    RouteLifecycle.DISCOVERED: (RouteLifecycle.PLANNED,),
    RouteLifecycle.PLANNED: (RouteLifecycle.REHEARSED, RouteLifecycle.GAVE_UP),
    RouteLifecycle.REHEARSED: (RouteLifecycle.ATTEMPTED, RouteLifecycle.GAVE_UP),
    RouteLifecycle.ATTEMPTED: (RouteLifecycle.SUCCEEDED, RouteLifecycle.GAVE_UP),
    RouteLifecycle.SUCCEEDED: (),
    RouteLifecycle.GAVE_UP: (),
}


def transition(current, nxt):
    if nxt not in _TRANSITIONS.get(current, ()):
        raise ValueError(
            f"Invalid transition from {current.name} to {nxt.name}"
        )
    return nxt
