"""
layout.py
---------
Fixed page and grid parameters.
All sizes in pixels at 96 DPI. One font, one size.
"""

# Page (A4 at 96 DPI)
PAGE_W = 794
PAGE_H = 1123

# Margins
MARGIN_LEFT   = 60
MARGIN_TOP    = 60
MARGIN_RIGHT  = 60
MARGIN_BOTTOM = 60

# Usable area
USABLE_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT   # 674
USABLE_H = PAGE_H - MARGIN_TOP  - MARGIN_BOTTOM  # 1003

# Font (monospace so every char is same width)
FONT_SIZE    = 12   # px
CHAR_WIDTH   = 7    # px per character
LINE_HEIGHT  = 20   # px  (font + leading)
WORD_GAP     = 4    # px between words

# Box = one full line across the usable width, height = one line
# This matches real text layout: fixed line spacing, ordered format
BOX_W = USABLE_W          # 674  (full usable width)
BOX_H = LINE_HEIGHT        # 20   (exactly one line tall)

# Each box is one line; boxes stack vertically
BOXES_COLS  = 1
BOXES_ROWS  = USABLE_H // BOX_H   # ~50 lines per page
TOTAL_BOXES = BOXES_ROWS           # 50

# Bits needed to store coordinates
import math
BITS_X = math.ceil(math.log2(BOX_W + 1))   # 10 bits (0-674)
BITS_Y = 0                                   # y is always 0 (one line per box)
BITS_Z = math.ceil(math.log2(TOTAL_BOXES))  # 6 bits  (0-49)
