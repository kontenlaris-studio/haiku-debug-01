#!/usr/bin/env python3
"""Write a debugging haiku (5-7-5, seventeen syllables) to /output/entry.txt."""
import os

HAIKU = """The bug is fixed now
but now the whole thing crashes
one fix, two new bugs"""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")

if __name__ == "__main__":
    main()
