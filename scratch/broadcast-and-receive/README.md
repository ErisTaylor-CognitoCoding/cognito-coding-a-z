# Broadcast and Receive

> **One sprite sends a signal — another sprite listens and reacts.**

---

## The analogy

A referee blows a whistle. All the players react — stop, freeze, look up. The referee doesn't talk to each player individually. They send one signal, and everyone who's listening responds.

That's broadcast and receive. One sprite broadcasts a message. Any other sprite (or the same one) that has a "when I receive" block reacts to it.

---

## The blocks

```scratchblocks
:: hat
when this sprite clicked
broadcast [game over v]

when I receive [game over v]
stop [all v]
```

Click the sprite → broadcast "game over" → everything that listens for "game over" responds. Clean separation between "something happened" and "what to do about it."

---

## Why it matters

This is event-driven programming — the same idea that powers button clicks in web apps, notifications on your phone, and message queues in server systems. In Python it's `events`, in JavaScript it's `addEventListener`. Scratch shows you the concept in the simplest possible form.

---

## Try it on Scratch

🔗 Scratch project coming soon — [subscribe to catch it](https://www.youtube.com/@CognitoCoding01).

---

## YouTube Short

🔜 Coming 19 Aug 2026 — the Scratch Concept Shorts series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
