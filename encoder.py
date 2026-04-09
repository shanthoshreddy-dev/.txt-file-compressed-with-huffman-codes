import re, math
from dictionary import build_dictionary
from layout import BOX_W, TOTAL_BOXES, CHAR_WIDTH, WORD_GAP, BITS_X, BITS_Z

def clean(text):
    return re.sub(r'[^a-z\s]', '', text.lower()).split()

def encode(input_path):
    text   = open(input_path, encoding='utf-8').read()
    CODES, REVERSE, stats = build_dictionary(text)
    tokens = clean(text)

    matrix = []
    page, cur_line, cursor_x = 1, 0, 0
    matrix.append([page, 0, 0, '0'])   # page separator: x=page_num, z=0, code='0'

    for tok in tokens:
        if tok not in CODES: continue
        code    = CODES[tok]
        word_px = len(tok) * CHAR_WIDTH

        if cursor_x + word_px > BOX_W:
            cur_line += 1; cursor_x = 0
        if cur_line >= TOTAL_BOXES:
            page += 1; cur_line = 0; cursor_x = 0
            matrix.append([page, 0, 0, '0'])

        matrix.append([cursor_x, 0, cur_line, code])
        cursor_x += word_px + WORD_GAP

    return matrix, page, CODES, REVERSE, stats

def matrix_size_bits(matrix):
    # x=BITS_X, z=BITS_Z, code=variable  (y omitted, always 0)
    fixed = BITS_X + BITS_Z
    total = sum(fixed + len(str(r[3])) if r[2]==0 and r[1]==0 and r[0]!=0
                else fixed + len(r[3]) for r in matrix)
    return total, fixed
