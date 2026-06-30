# Pumpkins Need Space

> **Check what's already there before you act on it.**

---

## The analogy

Pumpkins are high-maintenance. They need empty tiles next to them to spread. Plant one on a busy tile and it dies immediately.

So before you plant, you check: is this tile empty? Only if the answer is yes do you commit to planting. Otherwise you move on.

This is reading state before acting. Don't assume — check.

---

## Why it matters

In almost every real program, you verify before you commit. Is the user logged in before showing the dashboard? Is the file empty before writing to it? Is the tile clear before planting? Getting this wrong wastes cycles and breaks things silently.

---

## The code

```python
if get_entity_type() == Entities.NONE:
    plant(Entities.PUMPKIN)
```

The drone reads what's on the current tile. If it's empty (`NONE`), plant. If something's already there, skip entirely.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a third tile state like `"blocked"` and handle it with `elif`
- Try checking two conditions at once: `if tile == "empty" and space_next_to >= 1:`
- Change the values in the `tiles` list and see how the output shifts

---

## YouTube Short

🔜 Coming 1 Aug 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
