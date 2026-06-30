# Cactus Patience

> **Wait until a condition is true — don't act before it's ready.**

---

## The analogy

Cactus takes ages to grow. If you try to harvest too early, you get nothing. So you check. Not ready? Move on, come back later. Ready? Harvest.

This is patience built into code. You don't force it. You check, and when the time is right, you act.

---

## Why it matters

In the real world, timing matters. Don't send the email until the form is valid. Don't draw the button until the image has loaded. Don't harvest until the crop is done. `can_harvest()` is a guard — a check that says "not yet" until the moment it says "now."

---

## The code

```python
while True:
    if get_entity_type() == Entities.CACTUS:
        if can_harvest():
            harvest()
        else:
            move(North)  # come back next pass
    else:
        plant(Entities.CACTUS)
    move(East)
```

The drone skips unready cactus and revisits them on the next loop. No wasted harvests, no damaged plants.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `min_age` to 10 — what changes?
- Print how many passes it took before the item was ready
- Try a version where you keep checking the SAME item in a loop until it's ready (`while not ready`)

---

## YouTube Short

🔜 Coming 29 Aug 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
