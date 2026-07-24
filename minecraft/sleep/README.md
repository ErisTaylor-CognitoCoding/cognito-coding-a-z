# Sleep / Wait — Make the Turtle Pause

> **`os.sleep(N)` pauses the program for N seconds.**

---

## The analogy

Sometimes a program needs to wait — for a furnace to finish, for crops to grow, or just to slow down so you can see what's happening. `os.sleep(N)` does nothing for N seconds, then lets the program carry on.

---

## The code

```lua
print("Starting in 3 seconds...")
os.sleep(3)

turtle.dig()
turtle.forward()

print("Done.")
```

---

## Why it matters

Without sleep, turtles run at full speed. With it, you can watch each step, debug more easily, or time actions to match in-game events. Same idea as `time.sleep(3)` in Python.

---

## YouTube Short

🔜 Coming 31 Jul 2026 — [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01)
