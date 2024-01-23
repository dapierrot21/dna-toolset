from bio_structures import nucleotides
from utilities import coloring_nucleotides


class BioSequence:
    """DNA sequence class. Default value: ATCG, DNA No label"""

    def __init__(self, dna_sequence="ATCG", sequence_type="DNA", label="No Label"):
        """Sequence initialzation and sequence validation."""
        self.dna_sequence = dna_sequence.upper()
        self.label = label
        self.sequence_type = sequence_type
        self.is_valid = self.validate_sequence()
        assert (
            self.is_valid
        ), f"Provided data does not seem to be a correct {self.sequence_type} sequence."

    # Checkig the sequence to make sure it is a DNA string.

    def validate_sequence(self):
        """Checkig the sequence to make sure it is a DNA string."""
        return set(nucleotides).issuperset(self.dna_sequence)

    def show_sequence_info(self):
        """Returns Sequence Information"""
        return f"[Label]: {self.label}\n[Sequence]: {coloring_nucleotides(self.dna_sequence)}\n[Biotype]: {self.sequence_type}\n[Sequence Length]: {len(self.dna_sequence)}"
