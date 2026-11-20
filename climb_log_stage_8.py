# === Stage 8: Текстовый поиск ===
# Project: ClimbLog
def build_search_index(courses):
    """Construct a case-insensitive search index for course names."""
    index = {}
    for course in courses:
        key = course["name"].lower()
        index.setdefault(key, []).append(course)
    return index


def find_courses_by_name(index, needle):
    """Return all courses whose name contains the given substring.

    The search is case-insensitive. The needle is normalised to lowercase
    so that matching works regardless of the case used in the query.
    """
    needle = needle.strip().lower()
    if not needle:
        return []

    results = []
    for key, matches in index.items():
        if needle in key:
            results.extend(matches)
    return results


def highlight_matches(text, needle):
    """Return the original text with the first occurrence of the needle wrapped.

    Only the first match is highlighted to keep the output readable. If the
    needle is empty the text is returned unchanged.
    """
    if not needle:
        return text

    lower_text = text.lower()
    start = lower_text.find(needle)
    if start == -1:
        return text

    end = start + len(needle)
    return text[:start] + "\033[1m" + text[start:end] + "\033[0m" + text[end:]


def format_search_result(course, needle):
    """Render a single course entry for display in the search output."""
    highlighted_name = highlight_matches(course["name"], needle)
    return f"{highlighted_name} | {course['grade']} | {course['length']}m | {course['date']}"


def print_search_results(results, needle):
    """Print search results, one per line, highlighting matches in the name."""
    if not results:
        print(f"No courses found for '{needle}'.")
        return

    print(f"Found {len(results)} course(s) matching '{needle}':")
    for course in results:
        print(format_search_result(course, needle))
