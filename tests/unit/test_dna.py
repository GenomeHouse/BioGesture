import pytest

from packages.bioinformatics.src.dna import complement, gc_content, reverse_complement


def test_dna_helpers_normalize_input():
    assert complement(" acgt ") == "TGCA"
    assert reverse_complement("ACGT") == "ACGT"
    assert gc_content("ggccat") == pytest.approx(4 / 6)


def test_dna_helpers_reject_invalid_bases():
    with pytest.raises(ValueError, match="Invalid DNA bases"):
        complement("ACNX")
