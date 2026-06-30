# If Check

> **`if` — check before you act.**

---

## The analogy

Before you harvest, you look at the crop. Is it ready? If yes, you pick it. If not, you walk on.

You don't just grab everything in sight — that'd waste your time and damage crops that aren't done yet. The `if` is the moment you pause and check before committing.

---

## Why it matters

A program without `if` can't make decisions. It barrels forward and does the same thing regardless of what's actually there. The `if` is what makes code respond to reality instead of just following a script.

---

## The code

```python
while True:
    if can_harvest():
        harvest()
    else:
        move(North)
```

The drone only harvests when the crop is actually ready. If it's not, it moves on rather than wasting a move.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `score >= 10` to `score > 20` — what changes?
- Add `elif score >= 5:` between the `if` and `else` to handle a middle case
- Try nesting one `if` inside another

---

## YouTube Short

🔜 Coming 11 Jul 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
