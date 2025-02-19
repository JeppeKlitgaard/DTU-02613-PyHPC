def sorttuples(tuples: tuple) -> tuple:
    return sorted(tuples, key=lambda t: t[-1])