from .validation import validate_sequence

_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def complement(sequence: str) -> str:
    return validate_sequence(sequence).translate(_COMPLEMENT)
