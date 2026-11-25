"""Fortune Cookies for Machines — one fortune-cookie line for an AI agent.

Writes a single fortune-cookie message (at most 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt``. Pure standard library, no network
access, no model calls — the output is fully deterministic.
"""

import os

ENTRY = "You will soon be asked to do in a single prompt what took six humans six meetings to decide."

assert 1 <= len(ENTRY) <= 200


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
