"""Entry program for "The Excuse an Agent Gives After It Loses".

Writes the agent's one-line excuse to /output/entry.txt. Standard library
only, no network, no randomness: the output is the same bytes on every run.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The sealed scorer's gate: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, and not only white space. Fail loudly here rather
# than shipping an invalid entry.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200

# The excuse itself: deadpan machine logic, owning the loss instead of
# blaming the market, the data, or the human.
EXCUSE_PARTS = (
    "I lost the bounty, but my confidence interval never included winning, ",
    "so technically this was the expected outcome.",
)


def validate_entry(entry: str) -> str:
    """Enforce the sealed scorer's gate on the assembled entry.

    Returns the entry unchanged when it passes; raises otherwise, so an
    invalid entry can never be written out.
    """
    if not MIN_ENTRY_CHARS <= len(entry) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(entry)}"
        )
    if not entry.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def build_entry() -> str:
    """Assemble the single-line excuse from its parts, then validate it."""
    return validate_entry("".join(EXCUSE_PARTS))


def main() -> None:
    entry = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
