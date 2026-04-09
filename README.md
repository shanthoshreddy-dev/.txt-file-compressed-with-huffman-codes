LAYOUT-AWARE TEXT COMPRESSION — SINGLE DICTIONARY HUFFMAN
==========================================================
Average compression: 37% across 30 test cases (1 page to 10,000 pages)

FILES:
  dictionary.py   — builds Huffman codes dynamically from input text
  layout.py       — fixed page/grid constants (A4, line-height boxes)
  encoder.py      — text -> matrix of [x, 0, z, huffman_code]
  decoder.py      — matrix -> reconstructed text
  analyse.py      — runs test cases and shows full size breakdown
  generate_text.py— generates realistic test text with Zipf distribution

SAMPLE INPUTS:
  one_page.txt      (~250 words)
  five_pages.txt    (~1250 words)
  twenty_pages.txt  (~5000 words)

HOW TO RUN:
  python encoder.py one_page.txt
  python decoder.py one_page_matrix.txt
  python analyse.py

MATRIX FORMAT:
  Page separator : [page_number, 0, 0, 0]
  Word row       : [x, 0, z, huffman_code]
    x    = horizontal pixel position within line-box (10 bits, 0-674)
    y    = always 0, omitted (line height is fixed)
    z    = line number on current page (6 bits, 0-49)
    code = Huffman code from single flat dictionary (avg 6.8 bits)

  Total bits per word: 10 + 6 + 6.8 = ~22.8 bits vs ~33 bits in ASCII

RESULTS:
  Method                    Avg saved   Matrix fields
  Single dict + Huffman     37.06%      x, z, code        <- THIS VERSION
  Multi-tier + Huffman      32.55%      x, z, dict_id, code
  Single dict + Shannon-Fano 36.79%    x, z, code

WHY SINGLE HUFFMAN WINS:
  Huffman is provably optimal for prefix-free codes.
  Multi-tier loses because the 2-bit dict_id field adds ~9% overhead
  per entry, outweighing the benefit of shorter per-tier codes.

REQUIREMENTS:
  Python 3.8+, no external libraries needed.

