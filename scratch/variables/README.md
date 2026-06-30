# Variables in Scratch — Keeping Score

> **A named container that stores a number — and updates as the game runs.**

---

## The analogy

A scoreboard at a football match. The number starts at 0. Every time a goal goes in, it goes up by 1. The board doesn't know in advance what the final score will be — it just updates whenever something happens.

That's a variable. A named container. You give it a name (`score`), you give it a starting value (`0`), and you change it whenever the game tells you to.

---

## The blocks

```scratchblocks
when green flag clicked
set [score v] to (0)
forever
    if <touching [coin v]?> then
        change [score v] by (1)
    end
end
```

`score` starts at 0. Every time the sprite touches a coin, it goes up by 1. The scoreboard updates live on screen.

---

## Why it matters

This is the same concept as [variables in Python](../../variables/) — the idea is identical. A label, a value, and the ability to change it. Scratch just shows it visually as a scoreboard on the stage. Once you understand it here, the Python version is just different spelling.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 12 Aug 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
