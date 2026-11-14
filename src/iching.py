"""Small, hardware-independent core for a three-coin I Ching reading.

Lines are stored bottom first. Each coin contributes 2 or 3, so a line is
6 (old yin), 7 (young yang), 8 (young yin), or 9 (old yang).
"""

try:
    from random import getrandbits
except ImportError:
    from urandom import getrandbits


def cast_line(bit=getrandbits):
    return 6 + bit(1) + bit(1) + bit(1)


def cast(bit=getrandbits):
    return tuple(cast_line(bit) for _ in range(6))


def changed(lines):
    """Return the resulting six lines after old yin/yang change."""
    return tuple(7 if line == 6 else 8 if line == 9 else line for line in lines)


def draw(lines):
    """Render a reading in display order, with changing lines marked *."""
    symbols = {6: "---  --- *", 7: "---------", 8: "---  ---", 9: "--------- *"}
    return "\n".join(symbols[line] for line in reversed(lines))
