"""
decoder.py
----------
Reads the matrix file and reconstructs the original text
by reversing the huffman code lookup.
"""

from dictionary import REVERSE_CODES
from layout import BOXES_COLS, BOX_W, BOX_H, MARGIN_LEFT, MARGIN_TOP


def decode(matrix_path):
    entries = []
    with open(matrix_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 4:
                x, y, z, code = int(parts[0]), int(parts[1]), int(parts[2]), parts[3]
                entries.append((x, y, z, code))

    print(f"[A] Loaded {len(entries)} matrix entries")

    # Sort by z, then y, then x (reading order: box by box, line by line)
    entries.sort(key=lambda e: (e[2], e[1], e[0]))

    decoded_words = []
    errors = 0
    for x, y, z, code in entries:
        if code in REVERSE_CODES:
            decoded_words.append(REVERSE_CODES[code])
        else:
            print(f"  Unknown code: {code}")
            errors += 1

    print(f"[B] Decoded {len(decoded_words)} words  ({errors} errors)")
    print(f"[C] Reconstructed text (first 100 words):")
    print("    " + ' '.join(decoded_words[:100]))
    return decoded_words


if __name__ == '__main__':
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else 'sample_page_matrix.txt'
    decode(path)
