# Sunflowers — The Tallest Check

> **Keep track of the biggest value you've seen — by updating a variable as you go.**

---

## The analogy

You're walking a row of sunflowers. You want to find the tallest one. You can't see the whole row at once — you check each flower one at a time.

So you carry a number in your head: "tallest so far." Each time you see a taller one, you update your number. By the time you finish the row, that number IS the tallest.

That's a running maximum. One variable, updated as you loop.

---

## Why it matters

Finding the biggest (or smallest, or first, or last) thing in a collection is one of the most common problems in code. The pattern is always the same: start with a default, loop through everything, update when you find something better.

---

## The code

```python
tallest = 0

for x in range(get_world_size()):
    h = measure(Entities.SUNFLOWER)
    if h > tallest:
        tallest = h
    move(East)

print(tallest)
```

`tallest` starts at 0. Each iteration: measure the current sunflower, compare to the running record, update if it's bigger.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `heights` to include negative numbers — does it still work?
- Try finding the *smallest* value instead — what changes?
- Print the tallest value AND which position it was at

---

## YouTube Short

🔜 Coming 8 Aug 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
