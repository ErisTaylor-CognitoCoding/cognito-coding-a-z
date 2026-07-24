# Variables (Lua) — Give a Value a Name

> **`local x = 5` — store a value so you can use it later.**

---

## The analogy

A variable is a labelled box. You put a value in, give it a name, and refer to the name whenever you need the value. Change the box, everything that uses the name updates automatically.

---

## The code

```lua
local steps = 5
local message = "Turtle is moving!"

print(message)

for i = 1, steps do
    turtle.forward()
end
```

---

## Why it matters

`local` in Lua is the same idea as just naming a variable in Python — it keeps the variable scoped to where it's needed. Change `steps` in one place and the whole program adjusts.

---

## YouTube Short

🔜 Coming 28 Aug 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
