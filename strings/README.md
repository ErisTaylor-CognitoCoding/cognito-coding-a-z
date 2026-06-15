# Strings

> **Words the computer can hold and change.**

---

## The analogy

Imagine fridge magnets — the individual letter tiles you can rearrange on the fridge door. You can stick them together to make words, pull them apart, add more letters to the end, or swap a tile out.

A string is a line of those tiles. Letters, spaces, numbers — all stuck together in order and held in a variable.

---

## Why it matters

Almost everything a program handles eventually becomes text — names, messages, file contents, web pages. Knowing how to build, chop, and rearrange strings is one of the most-used skills in coding.

---

## The code

```python
name = "Ada"
greeting = "Hello, " + name + "!"
print(greeting)         # Hello, Ada!
print(len(greeting))    # 11
print(greeting.upper()) # HELLO, ADA!
```

The `+` sign glues two strings together. `len()` counts the characters. `.upper()` flips everything to capitals. Strings have dozens of built-in tricks like this.

---

## Try it

Open `python/example.py` and run it. Then:
- Change the name — the greeting updates automatically
- Try `.lower()` and `.replace("Ada", "World")`
- Print just the first three characters: `greeting[0:3]`

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
