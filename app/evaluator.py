from .analyzer import count_lines_of_code, count_keywords

def evaluate_versions(code1: str, code2: str) -> str:
    # Evaluate code by checking lines of code and number of control structures
    lines1 = count_lines_of_code(code1)
    lines2 = count_lines_of_code(code2)

    keywords1 = count_keywords(code1)
    keywords2 = count_keywords(code2)

    summary = []

    summary.append(f"Version 1: {lines1} lines, {keywords1} control structures")
    summary.append(f"Version 2: {lines2} lines, {keywords2} control structures")

    if keywords1 > keywords2:
        summary.append("Version 2 is simpler (fewer control structures).")
    elif keywords2 > keywords1:
        summary.append("Version 1 is simpler (fewer control structures).")
    else:
        summary.append("Both versions have similar complexity.")

    return "\n".join(summary)
