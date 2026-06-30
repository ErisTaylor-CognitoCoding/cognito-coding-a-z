# If Then Else — Decisions

> **Two paths. One check. The code takes the right one.**

---

## The analogy

A bouncer at a door: "Are you on the list? Yes → come in. No → stay out." One question, two outcomes. No grey area.

`if-then-else` works exactly like that. If the condition is true, run the first set of blocks. If it's false, run the second set. Only one of the two ever runs — never both.

---

## The blocks

```scratchblocks
when green flag clicked
forever
    if <touching [wall v]?> then
        set [color v] effect to (50)
        bounce off walls
    else
        set [color v] effect to (0)
    end
end
```

Touching a wall? Turn red and bounce. Not touching? Stay normal. The `else` covers everything the `if` doesn't.

---

## Why it matters

`if-else` is in every language. Python: `if x: ... else: ...`. JavaScript: `if (x) { } else { }`. The shape is the same everywhere. Scratch makes the two branches visually obvious — you can literally see the "true path" and the "false path" as separate blocks of code.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 9 Sep 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
