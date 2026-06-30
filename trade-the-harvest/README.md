# Trade the Harvest

> **Arithmetic — use maths to convert one thing into another.**

---

## The analogy

You've harvested 40 units of grass. The market gives you 3 gold per unit. How much do you make?

`40 × 3 = 120 gold.`

That's arithmetic in code. Addition, subtraction, multiplication, division — the four operations that let your program calculate things rather than just store them.

---

## Why it matters

Every financial calculation, every score system, every quantity conversion uses arithmetic. Price × quantity. Total - discount. Distance ÷ speed. These operations are the maths engine underneath almost every useful program.

---

## The code

```python
grass_held = num_items(Items.GRASS)
gold_per_unit = 3

if grass_held >= 10:
    trade(Items.GRASS, 10)
    gold_earned = 10 * gold_per_unit
    print(gold_earned)
```

Multiply units by price. Store the result. Use it to make decisions.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a 10% tax: `gold_after_tax = gold_earned * 0.9`
- Try integer division `//` — what's the difference from `/`?
- Calculate how many trades it would take to afford an upgrade that costs 500 gold

---

## YouTube Short

🔜 Coming 5 Sep 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
