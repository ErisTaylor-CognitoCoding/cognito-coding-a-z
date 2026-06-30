# Glide To — Smooth Movement

> **Move from one position to another over a set amount of time, smoothly.**

---

## The analogy

You want a sprite to float across the screen in 2 seconds, not teleport instantly. "Glide to" handles the in-between frames for you — it calculates where the sprite should be every moment of those 2 seconds.

Instant movement: `go to x y`. Smooth movement: `glide 2 secs to x y`. One block, totally different feel.

---

## The blocks

```scratchblocks
when green flag clicked
glide (2) secs to x: (200) y: (0)
glide (2) secs to x: (-200) y: (0)
```

The sprite glides right, then glides left. Two blocks. Looks polished without any extra maths.

---

## Why it matters

Smooth movement (interpolation/tweening) is everywhere in UI design — buttons sliding in, menus fading, game characters running. Libraries like CSS transitions, Flutter animations, and game engine tweens all do exactly what `glide to` does. Scratch makes you feel the difference before you learn the maths behind it.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 5 Aug 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
