def parse_int_list(input_str: str) -> list[int]:
    """Parse a space-separated string into a list of integers."""
    return [int(x) for x in input_str.strip().split()]