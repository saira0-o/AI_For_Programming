# reverse_complement.py
# Reads a single-line DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {
    "A": "T", "T": "A", "C": "G", "G": "C",
}

def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    sequence = []
    header_seen = False

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header_seen:
                    raise ValueError("Expected a single-record FASTA file")
                header_seen = True
                continue
            if not header_seen:
                raise ValueError("Expected a FASTA header before the sequence")
            sequence.append("".join(line.split()))

    if not header_seen:
        raise ValueError("No FASTA record found")
    return "".join(sequence)

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    try:
        return "".join(COMPLEMENT[nucleotide] for nucleotide in reversed(seq))
    except KeyError as error:
        raise ValueError(
            f"Invalid character in DNA sequence: {error.args[0]!r}; "
            "expected only A, T, C, or G"
        ) from error

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print the reverse complement of a FASTA sequence.")
    parser.add_argument("fasta", help="path to a single-record FASTA file")
    args = parser.parse_args()
    seq = read_fasta_sequence(args.fasta)
    print(reverse_complement(seq))
