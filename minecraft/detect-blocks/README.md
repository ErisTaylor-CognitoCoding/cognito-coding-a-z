# Detect Blocks — Look Before You Leap

> **Check if there's a block in front before trying to dig.**

---

## The analogy

Bumping into a wall without looking is a bug. `turtle.detect()` returns `true` if there's a block directly in front of the turtle. Use it inside an `if` to decide whether to dig or skip.

---

## The code

```lua
if turtle.detect() then
    turtle.dig()
    turtle.forward()
else
    print("Nothing to dig here.")
end
```

---

## Why it matters

Most real turtle programs need to handle obstacles. `detect()` before `dig()` means the turtle never wastes a move on empty air.

---

## YouTube Short

🔜 Coming 14 Aug 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
