# reverse_complement.py
# Reads a single-line DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}

def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    with open(path) as f:
        lines = f.readlines()
    return "".join(lines).replace("\n", "")

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    pass

if __name__ == "__main__":
    import sys
    seq = read_fasta_sequence(sys.argv[1])
    print(reverse_complement(seq))
