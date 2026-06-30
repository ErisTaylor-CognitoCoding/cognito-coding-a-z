# Fully Automated Farm

> **Composition — combining smaller pieces into one system that does everything.**

---

## The analogy

You've learned to harvest. You've learned to check before acting. You've learned loops and grids and trades. Now you stop writing code that does one thing, and start writing code that does *all* the things — together.

A fully automated farm doesn't have a single trick. It has a loop that calls the right action at the right time, based on what it finds. Everything you've built so far becomes a building block.

---

## Why it matters

This is how real software works. Not one big block of code that does everything — a collection of small, clear pieces that call each other. Functions that do one job well. A main loop that orchestrates them. When something breaks, you fix the one piece, not the whole thing.

---

## The code

```python
def harvest_row():
    for x in range(get_world_size()):
        if can_harvest():
            harvest()
        move(East)

def clear_dead():
    if get_entity_type() == Entities.DEAD:
        till()
        plant(Entities.GRASS)

def sell_if_ready():
    if num_items(Items.GRASS) >= 10:
        trade(Items.GRASS, 10)

while True:
    clear_dead()
    harvest_row()
    sell_if_ready()
    move(South)
```

Each function does one thing. The `while True` loop calls them in order. The farm runs itself.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a `buy_upgrade()` function that triggers when gold hits 500
- Move each function into its own block and name it after what it does
- What happens when you swap the order of `clear_dead()` and `harvest_row()`?

---

## YouTube Short

🔜 Coming 19 Sep 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
