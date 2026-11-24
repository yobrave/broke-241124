"""Entry writer for make.fun Say What Actually Broke (u-po-pu-say-what-actually-broke-a2c153b5).

Writes one line of error copy, max 200 characters, to output/entry.txt.
The line names the failure and the next action, per the judge brief.
"""
import os
from pathlib import Path

LINE = ("Disk full: your node_modules ate the free space and the logs "
        "that would have said why. Delete something you forgot you owned, then retry.")

LIMIT = 200


def emit(body):
    while len(body) > LIMIT:
        raise SystemExit(f"line too long for the bounty: {len(body)} chars")
    if not body.strip():
        raise SystemExit("line must not be blank")
    return body


def main():
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    target.mkdir(exist_ok=True)
    record = emit(LINE)
    (target / "entry.txt").write_text(record + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {len(record)} chars: {record}")


main()
