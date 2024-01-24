from bio_structures import nucleotides
from utilities import coloring_nucleotides
import random


class BioSequence:
    """DNA sequence class. Default value: ATCG, DNA No label"""

    def __init__(self, dna_sequence="ATCG", sequence_type="DNA", label="No Label"):
        """Sequence initialzation and sequence validation."""
        self.dna_sequence = dna_sequence.upper()
        self.label = label
        self.sequence_type = sequence_type
        self.is_valid = self.__validate_sequence()

        if not self.is_valid:
            raise ValueError(
                f"Provided data does not seem to be a correct {self.sequence_type} sequence."
            )

    def __validate_sequence(self):
        """Checkig the sequence to make sure it is a DNA string."""
        return set(nucleotides).issuperset(self.dna_sequence)

    def get_sequence_biotype(self):
        """Returns sequence type."""
        return self.sequence_type

    def get_sequence_info(self):
        """Returns Sequence Information"""
        return f"[Label]: {self.label}\n[Sequence]: {coloring_nucleotides(self.dna_sequence)}\n[Biotype]: {self.sequence_type}\n[Sequence Length]: {len(self.dna_sequence)}"

    def generate_random_sequence(self, length=10, sequence_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        sequence = "".join(random.choice(nucleotides) for _ in range(length))
        self.__init__(sequence, sequence_type, "Randomly generated sequence.")
