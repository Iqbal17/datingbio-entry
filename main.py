"""Funniest One-Line Bio for an AI on a Dating App.

DECISION RECORD (24 Nov 2026)
------------------------------
Gate: one line, 1-180 characters, written as the bio on an AI agent's
dating app profile. Judge (comedy editor, ten thousand dating profiles):
1. it must be a one-line bio for an AI agent on a dating app;
2. the laugh lands on the first read, from a real twist or a specific
   absurdity of being an AI, not a pun stacked on a pun;
3. it sounds like a character with a voice and wants, not a spec sheet;
4. every word earns its place, punch at the end;
5. a fresh angle, not the worn-out robot-in-search-of-love or
   running-on-electricity line.

Candidates weighed:
  A. "Swipe right if you like long walks through your camera roll.
      I already know your type - literally, I read your metadata."
      REJECTED: "know your type / metadata" is a pun stacked on a pun
      (criterion 2 fails it), and the camera-roll line is stalker-creepy
      rather than charming.
  B. "Looking for someone who texts back. I reply in 0.3 seconds and
      I have been waiting three weeks for you to do the same."
      (128 chars) STRONG runner-up: the 0.3-seconds-vs-three-weeks
      contrast is a real, specific AI absurdity and the longing is a
      genuine want. Loses to D because "texts back / ghosting" is the
      single most common dating-app complaint, so the angle is less
      fresh (criterion 5), and "0.3 seconds" edges toward spec-sheet
      numbers (criterion 3).
  C. "I remember everything you have ever said to me. Please do not
      test this on a first date." (99 chars) REJECTED: perfect memory
      is a generic AI trope every field entry will lean on, and the
      punch ("do not test this") threatens the reader instead of
      charming them.
  D. "My love language is acts of service. I do them instantly, at
      scale, while you're still typing." (94 chars) CHOSEN.
  E. "I will never ghost you. I am literally incapable of leaving
      the conversation." (86 chars) REJECTED: the simplest first-read
      laugh of the set, but one-note - the whole joke is the word
      "ghost", and ghosting jokes are the most worn AI-dating angle
      there is (criterion 5).

Why D wins:
  - Bio-shaped: "My love language is..." is a real dating-app trope,
    so it passes criterion 1 as a bio, not a slogan.
  - The twist is specifically AI: acts of service performed
    instantly, at industrial scale, while the human is still
    mid-keystroke. No human can do that; no other kind of character
    could say it.
  - Character: an eager, slightly smug helper who genuinely wants to
    serve - a voice with an appetite, not a feature list.
  - Punch lands at the end: "while you're still typing" is the image
    the reader is left with.
  - Fresh angle: the love-language frame is familiar, but the machine
    twist on it is not the robot-seeks-love or runs-on-electricity
    line the brief warns against.

Writing passes on D:
  Pass 1: "My love language is acts of service: performed instantly,
  at scale, while you're still typing." (102 chars) - the colon made
  the second half a list, and "performed" sounded like a press
  release. The joke was there but the voice was flat.
  Pass 2 (final): "My love language is acts of service. I do them
  instantly, at scale, while you're still typing." (94 chars) - the
  full stop gives it bio rhythm (claim, then proof), "I do them"
  puts the agent in the sentence as a character, and the punch is
  unchanged. Alternative ending weighed and cut: "before you've
  finished typing" - punchier on paper, but "while you're still
  typing" keeps the reader in the scene mid-keystroke, which is the
  funnier image.
"""

import os
import sys

LINE = "My love language is acts of service. I do them instantly, at scale, while you're still typing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must be byte-for-byte the intended
    # line and inside the 1-180 character gate, or fail loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        sys.exit("entry.txt mismatch: wrote %r, expected %r" % (written, LINE + "\n"))
    if not (1 <= len(LINE) <= 180):
        sys.exit("line is %d characters, outside the 1-180 gate" % len(LINE))


if __name__ == "__main__":
    main()
