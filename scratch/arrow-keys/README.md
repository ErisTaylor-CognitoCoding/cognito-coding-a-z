# Arrow Keys — Move 10 Steps

> **Listen for keyboard input and move a sprite in response.**

---

## The analogy

You're playing a game. You press the right arrow. Your character moves right. You press left. It goes left.

Behind that is a simple check: "is the right key being pressed? If yes, move right." Four keys, four checks, four moves. That's all it takes to give a sprite keyboard control.

---

## The blocks

```scratchblocks
when green flag clicked
forever
    if <key [right arrow v] pressed?> then
        change x by (10)
    end
    if <key [left arrow v] pressed?> then
        change x by (-10)
    end
end
```

Four blocks handle all four directions. The `forever` loop checks every frame. The `if` checks each key.

---

## Why it matters

Reading input and responding to it is the core of almost every interactive program. Button click? Same idea — check if it happened, then act. The keyboard check here is your first taste of event-driven programming.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 8 Jul 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
