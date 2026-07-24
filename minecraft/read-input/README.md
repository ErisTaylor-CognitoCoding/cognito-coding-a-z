# Read Input — Ask the Player a Question

> **Pause the program, wait for the player to type something, then use it.**

---

## The analogy

`read()` in Lua is the same idea as `input()` in Python. The program pauses, the player types, and the value comes back as a string. `tonumber()` converts it to a number if you need maths.

---

## The code

```lua
print("How many blocks shall I dig?")
local n = tonumber(read())

for i = 1, n do
    turtle.dig()
    turtle.forward()
end

print("Done!")
```

---

## Why it matters

Without input, the number of blocks is hardcoded. With `read()`, the player decides at runtime. Same idea as Python's `n = int(input("How many? "))`.

---

## YouTube Short

🔜 Coming 4 Sep 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
