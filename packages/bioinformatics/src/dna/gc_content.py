from .validation import validate_sequence


def gc_content(sequence: str) -> float:
    normalized = validate_sequence(sequence)
    return (normalized.count("G") + normalized.count("C")) / len(normalized)
