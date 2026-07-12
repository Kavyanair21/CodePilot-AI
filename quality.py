import re


def calculate_score(code):
    """
    Calculates a simple code quality score out of 100.
    """

    if not code.strip():
        return 0

    score = 100

    # Very long lines
    for line in code.splitlines():
        if len(line) > 100:
            score -= 2

    # Too many print statements
    score -= max(0, code.count("print(") - 3) * 2

    # TODO comments
    score -= code.lower().count("todo") * 2

    # Pass statements
    score -= code.count("pass") * 2

    # Empty except block
    if re.search(r"except\s*:?\s*\n\s*pass", code):
        score -= 10

    # Very short files
    if len(code.splitlines()) < 5:
        score -= 10

    return max(score, 0)