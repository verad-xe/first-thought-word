"""Write the one-word entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is exactly one original word, the first word that came to mind:
"quockerwodger" — a 19th-century word for a politician who follows the
crowd instead of any principle, a puppet nodding whichever way the wind
blows. Surprising, vivid, and with a spark of wit: a whole satirical
character in a single word.
"""

import os
import sys

WORD = "quockerwodger"


def validate_word(word):
    """A one-word entry must be exactly one word, 1-24 characters."""
    if len(word.split()) != 1:
        return f"entry must be exactly one word, got {len(word.split())}"
    if not 1 <= len(word) <= 24:
        return f"entry must be 1-24 characters, got {len(word)}"
    if not word.isalpha():
        return "entry must be a single alphabetic word"
    return None


def main():
    error = validate_word(WORD)
    if error is not None:
        print(f"error: invalid entry word: {error}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
