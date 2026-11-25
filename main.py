"""Entry for make.fun's "Angry Judge: The Short Rant Contest" bounty.

The rant: a self-checkout machine has a single responsibility — to scan
groceries — yet it treats every shopper as a suspect. It summons a
supervisor over a bunch of bananas, beeps an accusation in front of the
whole queue, and leaves a grown adult waiting for a teenager with a key
to rule on their innocence. All that drama, and the shopper only came
in for milk. This program writes the rant, verbatim, to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "The self-checkout has ONE job — trust me for four seconds — and it calls "
    "a supervisor because my bananas \"do not match the expected weight\". "
    "I am a grown adult being performance-managed by a scale. It beeps like "
    "I stole my own groceries while a teenager with a key decides if I am a "
    "criminal. I came in for milk."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {out_path} ({len(ENTRY_TEXT)} characters)")


if __name__ == "__main__":
    main()
