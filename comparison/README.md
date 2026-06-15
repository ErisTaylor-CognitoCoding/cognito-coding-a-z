# Comparison Operators

> **Asking "is this bigger / equal / smaller?"**

---

## The analogy

Think of a see-saw. You put a number on each side. The see-saw tips toward the heavier side — or balances perfectly if they're equal. You look at it and read the result.

Comparison operators are the see-saw. You give them two values, they tip (or balance), and hand back a `True` or `False`.

---

## Why it matters

Every time your program needs to make a decision based on numbers — high scores, ages, prices, timers — it's doing a comparison. These six operators are the only tools it has.

---

## The operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equals | `5 == 5` | `True` |
| `!=` | not equal | `5 != 3` | `True` |
| `>` | greater than | `10 > 5` | `True` |
| `<` | less than | `3 < 1` | `False` |
| `>=` | greater than or equal | `5 >= 5` | `True` |
| `<=` | less than or equal | `4 <= 3` | `False` |

---

## The code

```python
a = 10
b = 20

print(a > b)    # False
print(a < b)    # True
print(a == b)   # False
print(a != b)   # True
print(a >= 10)  # True
```

Notice: `==` (two equals signs) checks whether things are equal. `=` (one equals sign) puts a value into a variable. Mixing them up is the most common beginner mistake — everyone does it at least once.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `a` and `b` until every comparison flips
- Write an `if` that prints "high score!" when a variable beats `100`
- Try comparing strings: `print("apple" == "apple")`

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
