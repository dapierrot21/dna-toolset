def read_file(file_path):
    """Reading a file and returning a list of lines"""
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def guanine_cytosine_content(sequence):
    """GC Content in DNA/RNA sequence."""
    return round((sequence.count("C") + sequence.count("G")) / len(sequence) * 100, 6)


# Read data from the file (FASTA formatted file)
fasta_file = read_file(
    "/Users/deanpierrot/Desktop/dna-toolset/rosalind-problems/test_data/gc_content.txt"
)  # Storing file contents ina list.
fasta_dict = {}  # Dictionary for Labels & Data.
FASTA_LABEL = ""  # String for holding the current label


print(fasta_file)

# Clean/Prepare the data (Format for ease of you with our guanine_cytosine_content function)
for line in fasta_file:  # Converting FASTA/List file data into a dictionary
    if ">" in line:
        FASTA_LABEL = line
        fasta_dict[FASTA_LABEL] = ""
    else:
        fasta_dict[FASTA_LABEL] += line

print(fasta_dict)

# Format the data (Store the data in a convenient way)
# Run needed operation on the data (pass the data to our guanine_cytosine_content function)
## Using Dictionary Comprehension to generate a new dictionary with GC content.
result_dict = {
    key: guanine_cytosine_content(value) for (key, value) in fasta_dict.items()
}

print(result_dict)


## Looking for max value in values() of our new dictionary
max_gc_key = max(result_dict, key=result_dict.get)

# Collect results (Rosalind Submission in our case)
print(f"{max_gc_key[1:]}\n{result_dict[max_gc_key]}")
