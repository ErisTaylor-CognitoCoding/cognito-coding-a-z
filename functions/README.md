# Functions

> **A recipe you write once and reuse.**

---

## The analogy

Think of a recipe card for a cup of tea. You write the steps once:

1. Boil the water.  
2. Add the teabag.  
3. Pour into a mug.

After that, whenever anyone wants tea, you just say *"make tea"* — you don't list every step again. The card holds the steps. The phrase calls the card.

A function is that recipe card. You write the steps once inside it, then call it by name whenever you need it.

---

## Why it matters

Without functions, you'd copy-paste the same code everywhere. Change one thing and you'd have to hunt down every copy. With a function, you change it in one place and every call gets the update automatically.

---

## The code

```python
def make_tea():
    print("Boil water")
    print("Add teabag")
    print("Pour into mug")

make_tea()
make_tea()
```

`def` is short for "define" — you're writing the recipe. The two `make_tea()` lines at the bottom are the calls — each one runs all three steps.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a fourth step to the function — it appears in both calls automatically
- Write your own function called `greet()` that prints a welcome message
- Call it five times in a row

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
