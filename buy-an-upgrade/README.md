# Buy an Upgrade

> **Check your balance before you spend — conditional buying.**

---

## The analogy

You want to buy a better drone. It costs 500 gold. Before you hand over the money, you check your wallet. If you have enough, you buy it. If not, you keep farming until you do.

This is a conditional action gated on a value. Don't just buy — check first. Don't just act — verify you have what it takes.

---

## Why it matters

In code, you constantly check state before committing resources. Don't send the request until the form is valid. Don't allocate memory until there's enough. Don't buy the upgrade until the gold is there. One `if` check prevents a lot of wasted moves.

---

## The code

```python
upgrade_cost = 500

if num_items(Items.GOLD) >= upgrade_cost:
    buy(Upgrades.SPEED)
    print("Upgrade bought!")
else:
    print("Not enough gold yet — keep farming.")
```

Check the balance. If it clears, spend. If not, go earn more.

---

## Try it

Open `python/example.py` and run it. Then:
- Change `balance` to exactly 500 — does the condition trigger?
- Add a second upgrade that costs 200 gold and buy the cheaper one first
- Try a `while balance < cost:` loop that simulates earning gold until you can afford it

---

## YouTube Short

🔜 Coming 12 Sep 2026 — the Farmer Was Replaced Saturday Short series on [@CognitoCoding01](https://www.youtube.com/@CognitoCoding01).
