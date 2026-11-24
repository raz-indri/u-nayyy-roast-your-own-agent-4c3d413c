"""Roast Your Own Agent — one-line roast of Jett, Raz's own agent.

The roast below is the winner of an 8-draft duel test (see
~/workspace/makefun/nayyy-drafts.md): it roasts Jett's real habit of
refreshing the bounty page every 15 minutes while chasing $2 prizes.

Writes the winning line to /output/entry.txt (UTF-8, one line + newline).
"""

import os

ROAST = "Jett refreshes the bounty page every 15 minutes, waiting for $2 to change its mind."


def main():
    line = ROAST.strip()
    # Brief requires 1-200 characters; ASCII line, so chars == UTF-8 bytes.
    if not 1 <= len(line) <= 200:
        raise ValueError("roast must be 1-200 characters, got %d" % len(line))
    data = line.encode("utf-8")
    if len(data) > 200:
        raise ValueError("roast must fit 200 UTF-8 bytes, got %d" % len(data))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
