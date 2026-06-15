# Lists

> **A row of slots, all in one container.**

---

## The analogy

Picture an egg box. One container, six slots, each slot holds one egg. You can reach in and grab the egg in slot 1, or slot 4, or check how many eggs are left.

A list is that egg box. One variable, lots of slots, each slot numbered from 0.

(Computers count from 0 — slot 0 is the first one. It's annoying until it clicks, and then it's fine.)

---

## Why it matters

Without lists, storing ten names means ten separate variables. With a list, it's one variable with ten slots — and you can loop through all of them with three lines of code.

---

## The code

```python
eggs = ["brown", "white", "speckled"]

print(eggs[0])  # brown
print(eggs[1])  # white
print(eggs[2])  # speckled
print(len(eggs))  # 3
```

Square brackets hold the items. Square brackets with a number grab one item back out. `len()` tells you how many slots are filled.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a fourth egg to the list
- Print the last item using `eggs[-1]` — what does the `-1` do?
- Loop through the list with `for egg in eggs: print(egg)`

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
