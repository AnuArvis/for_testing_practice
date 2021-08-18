def get_strand(start: int, end: int) -> str:
    if not type(start) == type(end) == int:
        raise TypeError("must be integers")

    if start == end:
        raise ValueError("gene start cannot equal end")

    if min(start, end) < 0:
        raise ValueError("gene cannot have a negative coordinate")

    return "+" if start < end else "-"
