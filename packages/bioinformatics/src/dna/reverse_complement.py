from .complement import complement


def reverse_complement(sequence: str) -> str:
    return complement(sequence)[::-1]
