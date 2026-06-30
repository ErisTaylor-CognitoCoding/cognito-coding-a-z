# Forever Loop

> **A loop that runs continuously — checking, updating, animating — until the program stops.**

---

## The analogy

A game doesn't run once and stop. It keeps checking: is a key pressed? Did anything collide? Should the score update? It does this dozens of times a second, every second you're playing.

The `forever` block is Scratch's way of making this happen. Everything inside it repeats endlessly. It IS the game loop.

---

## The blocks

```scratchblocks
when green flag clicked
forever
    move (10) steps
    if on edge, bounce
end
```

The sprite bounces around the screen for as long as the flag is up. The `forever` never stops — you don't tell it when to end.

---

## Why it matters

In Python this is `while True:`. In JavaScript it's `requestAnimationFrame()`. Every game, every animation, every live dashboard uses a loop that runs continuously. The `forever` block makes that concept visible — you can *see* what goes inside the loop.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 15 Jul 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
