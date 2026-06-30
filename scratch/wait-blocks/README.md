# Wait Blocks — Pacing

> **Pause for a moment before the next thing happens.**

---

## The analogy

A good comedian times their punchline. A good game spaces its enemies. A good animation doesn't rush every frame. Timing matters — and `wait` gives you control over it.

Without `wait`, Scratch runs through blocks as fast as the computer allows — which is too fast to see. Adding a pause gives things room to breathe.

---

## The blocks

```scratchblocks
when green flag clicked
say [Ready?] for (2) seconds
say [Set...] for (1) seconds
say [GO!] for (0.5) seconds
```

Each message appears, stays visible for its duration, then the next one takes over. No wait blocks = all three would flash so fast you'd miss them.

---

## Why it matters

In code, pausing is genuinely tricky — you don't want to freeze the whole program, just delay one thing. Python has `time.sleep()`. JavaScript has `setTimeout()`. Game engines have `yield` and coroutines. Scratch's `wait` is the simplest form: stop here, count the seconds, then continue.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 16 Sep 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
