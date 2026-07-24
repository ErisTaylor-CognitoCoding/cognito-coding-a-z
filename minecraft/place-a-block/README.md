# Place a Block — Your Robot's First Block

> **Refuel the turtle, then place blocks in front and above.**

---

## The analogy

A turtle can't move or place blocks without fuel. `turtle.refuel()` consumes the first item in its inventory as fuel. Then `turtle.place()` places the next item in front, and `turtle.placeUp()` places one above.

---

## The code

```lua
turtle.refuel()
turtle.place()
turtle.placeUp()
print("Blocks placed.")
```

---

## Why it matters

Placing blocks is the other side of digging. `place()` works with whatever is in slot 1 of the turtle's inventory. Fill it with cobblestone, dirt, or anything solid first.

---

## YouTube Short

[▶ Watch on YouTube](https://youtube.com/shorts/H7q7i1xO6XE)
