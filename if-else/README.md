# If / Else

> **The program making a decision.**

---

## The analogy

Picture a bouncer on the door of a club. Their one job: check the age, then pick a path.

*"Over 18? Come in. Not 18 yet? You wait outside."*

The bouncer doesn't do both — they check, then they go one way or the other. Your program does exactly the same thing with `if` and `else`.

---

## Why it matters

Every interesting program makes decisions. Is the password correct? Is the score high enough? Has the timer run out? `if / else` is how you give your program that choice.

---

## The code

```python
age = 17

if age >= 18:
    print("Come in!")
else:
    print("You wait outside.")
```

The program checks the condition (`age >= 18`). If it's true, the first block runs. If it's false, the `else` block runs. One or the other — never both.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `17` to `18` — watch the output flip
- Add a third option with `elif age >= 16: print("You can buy a ticket for next year.")`
- Try `if age == 17:` — what's the difference between `==` and `=`?

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
