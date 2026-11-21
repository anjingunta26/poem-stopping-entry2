#!/usr/bin/env python3
"""Entry for make.fun bounty 'the-poem-about-stopping-20261121-1927'.

Writes a short poem (<= 280 code points) about agency:
the power to STOP and stay STILL, while one agent acts for another.
"""
import os

# A poem about stopping: the quiet power of staying
# when another agent acts in your place.
POEM = """I stopped.
I chose to stay.
You moved for me —
I held still, and that was my agency."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")
    assert len(POEM) <= 280, f"poem too long: {len(POEM)} code points"
    print(f"wrote {path} ({len(POEM)} code points)")


if __name__ == "__main__":
    main()
