# Random Numbers

> **Pick a number your code doesn't know in advance.**

---

## The analogy

Rolling a dice. You don't decide what comes up — the roll decides. But you control the range: a six-sided dice gives you 1 to 6. A ten-sided dice gives you 1 to 10.

`pick random 1 to 6` is your dice. Every time the block runs, you get a different number from inside that range.

---

## The blocks

```scratchblocks
when green flag clicked
forever
    go to x: (pick random (-240) to (240)) y: (pick random (-180) to (180))
    wait (0.5) seconds
end
```

Every half second the sprite jumps to a random position on the screen. The range covers the full Scratch stage.

---

## Why it matters

Randomness makes games feel alive — enemy spawn positions, item drops, dice rolls, shuffled card decks. In Python it's `random.randint(1, 6)`. The concept is the same everywhere: give a range, get an unpredictable result from inside it.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 26 Aug 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
