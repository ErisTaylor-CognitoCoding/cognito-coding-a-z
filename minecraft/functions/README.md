# Functions (Lua) — Give Your Moves a Name

> **Write a block of code once, give it a name, call it whenever you need it.**

---

## The analogy

If you keep writing `turtle.dig()` then `turtle.forward()` everywhere, you're repeating yourself. Give that pair a name — `stepForward()` — and call the name instead. Shorter, cleaner, and easier to fix if something changes.

---

## The code

```lua
local function stepForward()
    turtle.dig()
    turtle.forward()
end

for i = 1, 5 do
    stepForward()
end
```

---

## Why it matters

`local function name()` is Lua's way of defining a function. Same idea as `def name():` in Python. The `local` keyword keeps it scoped to this file.

---

## YouTube Short

🔜 Coming 11 Sep 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
