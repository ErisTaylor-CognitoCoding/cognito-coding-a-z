# Forever Loop (Lua) — while true do

> **A loop that never stops unless you break it or stop the program.**

---

## The analogy

`while true do` in Lua is the same idea as `while True:` in Python. The condition is always true, so the loop runs forever. Useful for turtles that should keep working until you stop them.

---

## The code

```lua
while true do
    turtle.dig()
    turtle.forward()
    os.sleep(0.5)
end
```

---

## Why it matters

Most useful turtle programs run until you interrupt them — mining, farming, patrolling. `while true do` is the standard way to write that. `os.sleep(0.5)` adds a pause so you can watch what's happening.

---

## YouTube Short

🔜 Coming 18 Sep 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
