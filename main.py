"""A tiny program that drops a single first-thought word into the output file.

The competition asks for one word and nothing else, so this script does the
simplest possible thing: it holds one word and writes it verbatim to the
expected output path. No punctuation, no extra lines, no trailing newline.
"""

from pathlib import Path

# The word that surfaced first: a guide who escorts souls onward.
ENTRY = "psychopomp"

# The format gate only allows a short, non-blank single word, so these
# checks run before any file is touched.
assert 1 <= len(ENTRY) <= 24, "entry must be between 1 and 24 characters"
assert ENTRY.strip() == ENTRY and " " not in ENTRY, "entry must be one word"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
