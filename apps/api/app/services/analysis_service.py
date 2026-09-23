from ..schemas.analysis import (
    ComplementResult,
    GCContentResult,
    ORFAnalysisResult,
    ORFResult,
    ProteinTranslationResult,
)
from ..schemas.sequence import SequenceDetail

_COMPLEMENT = str.maketrans("ACGTN", "TGCAN")
_CODONS = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*", "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def gc_content(sequence: SequenceDetail) -> GCContentResult:
    counts = {base: sequence.sequence.count(base) for base in "ACGTN"}
    gc = counts["G"] + counts["C"]
    at = counts["A"] + counts["T"]
    return GCContentResult(
        sequence_id=sequence.id,
        length=sequence.length,
        gc_content=round(gc / sequence.length * 100, 2),
        at_content=round(at / sequence.length * 100, 2),
        counts=counts,
    )


def complement(sequence: SequenceDetail) -> ComplementResult:
    direct = sequence.sequence.translate(_COMPLEMENT)
    return ComplementResult(sequence_id=sequence.id, complement=direct, reverse_complement=direct[::-1])


def find_orfs(sequence: SequenceDetail, minimum_length: int = 9) -> ORFAnalysisResult:
    results: list[ORFResult] = []
    value = sequence.sequence
    for frame in range(3):
        start = frame
        while start <= len(value) - 3:
            if value[start:start + 3] != "ATG":
                start += 3
                continue
            end = start + 3
            while end <= len(value) - 3 and value[end:end + 3] not in {"TAA", "TAG", "TGA"}:
                end += 3
            if end <= len(value) - 3 and end + 3 - start >= minimum_length:
                results.append(ORFResult(start=start, end=end + 3, frame=frame, sequence=value[start:end + 3]))
            start = end + 3
    return ORFAnalysisResult(sequence_id=sequence.id, orfs=results)


def translate(sequence: SequenceDetail, frame: int = 0) -> ProteinTranslationResult:
    if frame not in (0, 1, 2):
        raise ValueError("Frame must be 0, 1, or 2")
    protein = "".join(_CODONS.get(sequence.sequence[index:index + 3], "X") for index in range(frame, sequence.length - 2, 3))
    return ProteinTranslationResult(sequence_id=sequence.id, frame=frame, protein=protein)
