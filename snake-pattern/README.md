# Snake Pattern — Nested Loops

> **A loop inside a loop — to cover every tile in a grid.**

---

## The analogy

One loop covers a single row. But a field is a grid — rows AND columns.

The snake pattern uses two loops stacked. The outer loop moves you down to the next row. The inner loop moves you across it. Together they touch every single tile — efficiently, no tile missed, no tile doubled.

Snake-shaped because you go left→right on row 1, then right→left on row 2, then left→right on row 3. Like a snake winding through the field.

---

## Why it matters

Grids are everywhere — game boards, spreadsheets, pixel art, maps, image data. Nested loops are the standard way to process every cell in a 2D structure. Learn this shape once, use it in every language forever.

---

## The code

```python
for y in range(get_world_size()):
    for x in range(get_world_size()):
        harvest()
        if x < get_world_size() - 1:
            move(East)
    move(South)
```

Outer loop: step down one row at a time. Inner loop: harvest across the row. Together: every tile covered.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `COLS` to 4 — how does the output change?
- Print coordinates `(row, col)` instead of a dot
- Try removing the inner loop entirely — what happens?

---

## YouTube Short

🔜 Coming 25 Jul 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
