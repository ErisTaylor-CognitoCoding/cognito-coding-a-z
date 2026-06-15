# Booleans

> **True or false — on or off.**

---

## The analogy

A light switch. That's it. It's either on or it's off. There's no "sort of on". No "a bit off". Two states, always one of them, never neither.

A boolean is a light switch in code. It holds exactly one of two values: `True` or `False`. You use them to track states — is the player alive? Is the door open? Has the game started?

---

## Why it matters

Booleans are the foundation of every decision a program makes. The `if` statement you already know? It checks whether something is `True` or `False`. Every comparison you run produces a boolean result.

---

## The code

```python
light_on = True
print(light_on)   # True

light_on = False
print(light_on)   # False

print(10 > 5)     # True
print(10 < 5)     # False
```

`True` and `False` must be written with a capital first letter — Python is picky about that. The comparisons at the bottom (`>`, `<`) produce boolean values as their answer.

---

## Try it

Open `python/example.py` and run it. Then:
- Try `print(10 == 10)` and `print(10 == 11)`
- Create a variable `game_over = False`, then write an `if` that checks it
- Try `print(not True)` — what does `not` do?

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
