# Dig a Tunnel — turtle.dig() in a For Loop

> **Use a for loop to dig a straight tunnel without repeating yourself.**

---

## The analogy

Writing `turtle.dig()` then `turtle.forward()` ten times in a row works, but a `for` loop does the same job in two lines. One number controls how long the tunnel is.

---

## The code

```lua
for i = 1, 10 do
    turtle.dig()
    turtle.forward()
end
```

---

## Why it matters

`for i = 1, N do` is the standard Lua counting loop. Change `10` to any number and the tunnel changes length. Same idea as `for i in range(10):` in Python.

---

## YouTube Short

[▶ Watch on YouTube](https://youtube.com/shorts/iXwzDlBLbN0)
