# If Touching — Collision Detection

> **Check if two things are overlapping — then react.**

---

## The analogy

In a game of Pong, the ball hits the paddle and bounces. How does the program know they touched?

It checks. Every frame, it asks: "is the ball touching the paddle right now?" If yes, reverse the direction. If no, keep going. That continuous check — "are these two things touching?" — is collision detection.

---

## The blocks

```scratchblocks
when green flag clicked
forever
    if <touching [paddle v]?> then
        set rotation style [left-right v]
        turn (180) degrees
    end
end
```

Every frame: check. If touching: bounce. Otherwise: nothing. One `if` inside a `forever` loop handles the whole thing.

---

## Why it matters

Collision detection shows up everywhere physics matters — games, simulations, robot navigation. In more advanced code you'd calculate bounding boxes or pixel overlaps. In Scratch, `touching?` does the hard maths for you so you can learn the *concept* without the geometry.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 22 Jul 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
