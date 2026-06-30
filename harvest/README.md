# Harvest — While True

> **`while True` — a loop that never stops until something shuts it down.**

---

## The analogy

You're a farmer. Every morning you walk out, check the field, harvest what's ready, and go home. Then the next day you do it again. And again. And again — for the rest of your life.

Nobody tells you when to stop. You just keep going until the farm closes.

That's `while True`. It doesn't check a condition before each loop. It just runs forever — until a `break` or an error stops it.

---

## Why it matters

Most real programs don't run once and quit. A game loop keeps checking for input. A web server keeps waiting for requests. A background agent keeps watching for new tasks. Every single one is `while True` underneath.

---

## The code

In The Farmer Was Replaced, the drone runs your code on repeat automatically — but the logic is exactly this:

```python
while True:
    harvest()
```

Every tick: harvest. Every tick: harvest. Every tick: harvest. The drone never takes a day off.

---

## Try it

Open `python/example.py` and run it. Then:
- Add a counter variable that increases by 1 every loop — print it
- Try `if counter > 5: break` to make it stop after 5 runs
- Replace the `print` with two different messages and alternate them

---

## YouTube Short

🔜 Coming 4 Jul 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
