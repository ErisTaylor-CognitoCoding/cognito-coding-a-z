# Print to Screen — Show a Message on the Turtle

> **Send text to the terminal so you know what the turtle is doing.**

---

## The analogy

`print()` in Lua works the same as `print()` in Python — it sends text to the terminal. Useful for debugging or showing the turtle's status while it runs.

---

## The code

```lua
print("Hello from the turtle!")
print("Fuel level: " .. turtle.getFuelLevel())
```

---

## Why it matters

The `..` operator joins strings in Lua. `turtle.getFuelLevel()` returns a number — joining it to a string lets you print both together. Knowing the fuel level stops you wondering why the turtle stopped mid-job.

---

## YouTube Short

🔜 Coming 7 Aug 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
