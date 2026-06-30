# Trees — Multi-Resource Harvest

> **`if / elif` — one check, multiple possible outcomes.**

---

## The analogy

A tree gives you different things depending on the season. Spring: flowers. Summer: fruit. Autumn: wood. Winter: nothing.

You don't need four separate programs. You check once, and branch to the right action. `if` handles the first case, `elif` handles each alternative, `else` mops up anything you didn't plan for.

---

## Why it matters

Most real decisions have more than two paths. "If premium user, show dashboard. Else if trial, show limited view. Else show login." That's `if / elif / else`. It's the cleanest way to write one decision with many outcomes — without nesting loads of `if`s inside each other.

---

## The code

```python
entity = get_entity_type()

if entity == Entities.TREE:
    if can_harvest():
        harvest()
elif entity == Entities.BUSH:
    harvest()
elif entity == Entities.NONE:
    plant(Entities.TREE)
```

One sweep. One check per tile. Each `elif` handles a different resource without repeating the whole structure.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a fourth option: `"mushroom"` — print a different message
- Move the `elif` blocks around — does the order matter?
- What happens if you remove the `else` entirely?

---

## YouTube Short

🔜 Coming 22 Aug 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
