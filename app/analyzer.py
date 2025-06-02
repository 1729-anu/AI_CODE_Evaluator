def count_lines_of_code(code: str) -> int:
    return len([line for line in code.split('\n') if line.strip()])

def count_keywords(code: str, keywords=None) -> int:
    if keywords is None:
        keywords = ['for', 'while', 'if', 'def', 'class']
    return sum(code.count(keyword) for keyword in keywords)
