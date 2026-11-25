"""The Battery's Last Text to Its Charger.

A tiny deterministic program: it writes the phone battery's final
text message to its charger into ``entry.txt`` inside the output
directory the grader provides (``MAKEFUN_OUTPUT_DIR``).

Pure standard library only; no network, no randomness, no input.
The message is one line, well under 200 characters, and ends on
its punchline: the battery is not dying, it is walking out.
"""

import os

MESSAGE = (
    "hey, it's me, 1%. spent all day watching you charge everything "
    "else first. so when the screen goes black in 3... 2... don't "
    "call it dying. call it me leaving you."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MESSAGE)


if __name__ == "__main__":
    main()
