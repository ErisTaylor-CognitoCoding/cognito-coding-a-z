# Input / Output

> **The program listening and talking back.**

---

## The analogy

A walkie-talkie. You press the button and talk — that's input. The other person replies and you hear it — that's output. Two-way communication. You talk to the program, the program talks back.

Without input, a program can't respond to the person using it. Without output, you'd never know what it worked out. Together they're how a program and a human have a conversation.

---

## Why it matters

Every app, game, and website you've ever used runs on this loop: take input from the user, do something with it, give output back. It's the heartbeat of interactive software.

---

## The code

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

`input()` pauses the program, shows your message, and waits for the user to type something and press Enter. Whatever they type comes back as a string and gets stored in `name`. `print()` is output — it sends text back to the screen.

---

## Try it

Open `python/example.py` and run it. Type your name when it asks.

Then:
- Add a second `input()` asking for their favourite colour and use it in the reply
- Try `age = int(input("How old are you? "))` — what does `int()` do, and why do you need it?
- Write a tiny quiz: ask a question, check the answer with `if`, print "Correct!" or "Try again!"

---

## YouTube Short

🔜 Coming soon — subscribe at [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01) to catch it.
