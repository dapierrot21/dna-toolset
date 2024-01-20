def coloring_nucleotides(sequence):
    nucleotide_colors = {
        "A": "\033[92m",
        "C": "\033[94m",
        "G": "\033[93m",
        "T": "\033[91m",
        "U": "\033[91m",
        "reset": "\033[0;0m",
    }

    temp_str = ""

    for nucleotide in sequence:
        if nucleotide in nucleotide_colors:
            temp_str += nucleotide_colors[nucleotide] + nucleotide
        else:
            temp_str += nucleotide_colors["reset"] + nucleotide
    return temp_str + "\033[0;0m"
