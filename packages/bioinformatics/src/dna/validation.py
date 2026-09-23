VALID_BASES = frozenset("ACGT")


def validate_sequence(sequence: str) -> str:
    """Return a normalized DNA sequence or raise ValueError."""
    normalized = sequence.strip().upper()
    if not normalized:
        raise ValueError("DNA sequence cannot be empty")
    invalid = set(normalized) - VALID_BASES
    if invalid:
        raise ValueError(f"Invalid DNA bases: {''.join(sorted(invalid))}")
    return normalized
