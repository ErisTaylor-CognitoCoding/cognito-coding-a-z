# Grass Strip — For Loop

> **`for` — do something once for every item in a collection.**

---

## The analogy

You have a row of 10 tiles to harvest. You could write `harvest()` ten times. But what if the row grows to 100? To 1,000?

A `for` loop says: "for every tile in this row, do the thing." One instruction. Covers the whole strip. Grow the row — the code doesn't change.

---

## Why it matters

Whenever you have a collection of things to work through — tiles, names, orders, search results — a `for` loop covers all of them in one go. You write it once, it handles any size.

---

## The code

```python
for i in range(get_world_size()):
    harvest()
    move(East)
```

The loop runs once per tile in the row. Harvest. Move. Harvest. Move. Until the strip is done — however wide it is.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `range(5)` to `range(10)` — how many lines print?
- Try `for item in ["apple", "banana", "cherry"]:` and print each one
- Print the loop number (`i`) alongside the item so you can see the count

---

## YouTube Short

🔜 Coming 18 Jul 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
