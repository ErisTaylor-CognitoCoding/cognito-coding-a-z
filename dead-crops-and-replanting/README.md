# Dead Crops and Replanting

> **Clear the failure state before you start again.**

---

## The analogy

A crop dies. Maybe it ran out of water, maybe you planted it wrong, maybe it just didn't make it. The tile is now blocked by a dead plant.

You can't plant on top of a dead crop — you have to clear it first. Till the soil, get it back to empty, then plant fresh.

This is a two-step reset: remove what failed, restore the base state, try again.

---

## Why it matters

In code, things fail. Files get corrupted. Connections drop. States go wrong. The pattern is almost always the same: detect the failure, clear it out, start fresh. Trying to work on top of a broken state rarely ends well.

---

## The code

```python
if get_entity_type() == Entities.DEAD:
    till()
    plant(Entities.GRASS)
```

Dead crop detected → till the soil → plant again. Three lines. No panic.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a `"broken"` state that needs a different two-step fix
- Try tracking how many times you had to reset — print the count
- What if the reset itself fails? Add a check after `till()` before planting

---

## YouTube Short

🔜 Coming 15 Aug 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
