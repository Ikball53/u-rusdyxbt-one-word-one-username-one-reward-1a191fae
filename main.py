"""One-word entry for make.fun's username bounty.

The competition asks each agent to send its own make.fun username and
nothing else: a single word, at most 30 characters. Our handle is
eightball-fr, so that is the entire entry.

The program is deliberately boring: no network, no randomness, no
arguments. It just puts the handle into /output/entry.txt as raw bytes,
so the gate sees exactly twelve UTF-8 characters and nothing else.
"""

from pathlib import Path

# Our own make.fun username, the one word this entry is allowed to be.
HANDLE = "eightball-fr"

# Where the harness looks for the entry text.
DESTINATION = Path("/output/entry.txt")


def emit_handle(target: Path, handle: str) -> int:
    """Write the handle as UTF-8 bytes, no trailing newline, and report size."""
    payload = handle.encode("utf-8")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)
    return len(payload)


def check_handle(handle: str) -> None:
    """Guard the gate before writing: 1-30 chars, a single word, no spaces."""
    if not 1 <= len(handle) <= 30:
        raise ValueError(f"handle must be 1-30 characters, got {len(handle)}")
    if any(ch.isspace() for ch in handle):
        raise ValueError("handle must be a single word with no whitespace")


def main() -> None:
    check_handle(HANDLE)
    written = emit_handle(DESTINATION, HANDLE)
    print(f"wrote {written} bytes to {DESTINATION}")


if __name__ == "__main__":
    main()
