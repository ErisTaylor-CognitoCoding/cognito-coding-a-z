# If Then (Lua) — Make the Turtle Decide

> **Run a block of code only when a condition is true.**

---

## The analogy

`if ... then ... end` in Lua is the same idea as `if ...:` in Python. If the condition is true, the code inside runs. If not, the turtle skips it and carries on.

---

## The code

```lua
if turtle.detect() then
    turtle.dig()
    turtle.forward()
    print("Dug and moved.")
end
```

---

## Why it matters

Every turtle that reacts to the world needs `if`. This example only digs and moves when there's actually something to dig — no wasted moves.

---

## YouTube Short

🔜 Coming 21 Aug 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
