# Conditional buying — check before you spend
# Run this: python buy-an-upgrade/python/example.py

balance = 350
upgrade_cost = 500

print(f"Balance: {balance}g  |  Upgrade cost: {upgrade_cost}g")

if balance >= upgrade_cost:
    balance = balance - upgrade_cost
    print(f"Upgrade bought! Remaining: {balance}g ✅")
else:
    shortfall = upgrade_cost - balance
    print(f"Not enough gold — need {shortfall}g more ⏳")

# Bonus: simulate farming until you can afford it
print("\n--- Saving up ---")
balance = 0
gold_per_harvest = 30

while balance < upgrade_cost:
    balance = balance + gold_per_harvest
    print(f"  Earned {gold_per_harvest}g → balance: {balance}g")

print(f"Bought the upgrade! 🎉")

# In The Farmer Was Replaced, it looks like this:
#
# if num_items(Items.GOLD) >= 500:
#     buy(Upgrades.SPEED)
