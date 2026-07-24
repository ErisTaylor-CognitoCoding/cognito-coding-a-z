# Dig Down — One Word, One Hole

> **One command digs one block down. A loop makes it a shaft.**

---

## The analogy

`turtle.digDown()` digs the block below the turtle. On its own it digs one block. Wrap it in a `for` loop and the turtle digs a shaft as deep as you tell it.

---

## The code

```lua
for i = 1, 10 do
    turtle.digDown()
    turtle.down()
end
```

---

## Why it matters

The loop version is more useful than a single `digDown()` call. Control the depth by changing `10`. The turtle digs down and moves down together — otherwise it just digs the same block again and again.

---

## YouTube Short

[▶ Watch on YouTube](https://youtube.com/shorts/cfFXAYphEes)
