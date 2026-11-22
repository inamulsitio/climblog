# === Stage 12: Постраничный вывод ===
# Project: ClimbLog
from typing import List, Dict, Any


DEFAULT_PAGE_SIZE = 20

class Page:
    def __init__(self, page: int, page_size: int, items: List[Any], total: int):
        self.page = page
        self.page_size = page_size
        self.items = items
        self.total = total

    @property
    def total_pages(self) -> int:
        if self.page_size <= 0:
            return 0
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_prev(self) -> bool:
        return self.page > 1

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    def to_dict(self) -> Dict[str, Any]:
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total": self.total,
            "total_pages": self.total_pages,
            "items": self.items,
            "has_prev": self.has_prev,
            "has_next": self.has_next,
        }


def paginate(items: List[Any], page: int, page_size: int) -> Page:
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = DEFAULT_PAGE_SIZE
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size
    return Page(page, page_size, items[start:end], total)


def page_navigation(page: int, total_pages: int) -> str:
    if total_pages <= 1:
        return "No pagination needed."
    if page == 1:
        arrow = "»"
    elif page == total_pages:
        arrow = "«"
    else:
        arrow = "«»"
    return f"Page {page} of {total_pages} {arrow}"
