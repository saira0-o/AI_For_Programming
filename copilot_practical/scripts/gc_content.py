"""Report GC content for each record in a FASTA file."""

import argparse
import sys


def fasta_records(path):
    """Yield (header, sequence) pairs from a multi-record FASTA file."""
    header = None
    sequence = []

    with open(path) as fasta:
        for line in fasta:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence)
                header = line[1:].strip()
                sequence = []
            else:
                if header is None:
                    raise ValueError("Expected a FASTA header before the sequence")
                sequence.extend(line.split())

    if header is not None:
        yield header, "".join(sequence)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content for each record in a FASTA file."
    )
    parser.add_argument("fasta", help="path to a FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        default=0.0,
        help="only print records with GC content above this percentage",
    )
    args = parser.parse_args()

    for header, sequence in fasta_records(args.fasta):
        if not sequence:
            print(f"Warning: skipping empty sequence for >{header}", file=sys.stderr)
            continue
        gc_percent = 100 * sum(base in "GgCc" for base in sequence) / len(sequence)
        if gc_percent <= args.min_gc:
            continue
        print(f">{header}\tGC content: {gc_percent:.2f}%")


if __name__ == "__main__":
    main()
