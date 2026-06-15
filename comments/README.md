# Comments

> **Notes to humans — the computer ignores them completely.**

---

## The analogy

You know how teachers leave sticky notes in the margins of a book? Little reminders: *"this bit is tricky"*, *"remember this for the exam"*, *"ask if confused"*. The book still reads the same — those notes are just for the next person who opens it.

Comments are sticky notes in your code. You write them for yourself (or your teammates). The computer walks straight past them as if they aren't there.

---

## Why it matters

Code that made sense when you wrote it can look like a foreign language three weeks later. A well-placed comment ("this part resets the score at the start of each level") saves you from reading ten lines of code trying to remember what you were thinking.

---

## The code

```python
# This is a comment — the computer ignores it
score = 0  # Start the player at zero

# Add 10 points for picking up the coin
score = score + 10

print(score)  # Should print 10
```

Everything after a `#` on the same line is a comment. Short, honest notes are better than long explanations — the code should do most of the talking.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a comment above the `print` line explaining what it does
- Try commenting *out* the `score = score + 10` line (put `#` at the start) — watch what prints
- Write a comment that describes what the whole file does

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
