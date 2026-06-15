# Loops

> **Doing something again without writing it again.**

---

## The analogy

Imagine telling your dog to fetch. If you want it to fetch five times, you could say:

*"Fetch. Fetch. Fetch. Fetch. Fetch."*

Or you could say:

*"Fetch — five times."*

That second version is a loop. One instruction, run again and again until the count is done.

---

## Why it matters

Programs repeat things constantly — counting down, checking every item in a list, sending the same message to a thousand users. Loops let you write the instruction once and let the computer do the repeating.

---

## The code

```python
for i in range(5):
    print("fetch!")
```

`range(5)` counts from 0 to 4 — five numbers, five repeats. The indented line underneath runs each time. Change `5` to `100` and it runs a hundred times. Same code, no rewriting.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `5` to `10`
- Change `"fetch!"` to your own message
- Print `i` inside the loop — watch what number it is each time

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
