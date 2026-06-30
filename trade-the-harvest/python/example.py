# Arithmetic — convert one thing into another using maths
# Run this: python trade-the-harvest/python/example.py

grass_units = 40
gold_per_unit = 3

gold_earned = grass_units * gold_per_unit
print(f"Traded {grass_units} grass for {gold_earned} gold 💰")

# Now apply a 10% market fee
fee = gold_earned * 0.1
gold_after_fee = gold_earned - fee
print(f"After 10% market fee: {gold_after_fee:.0f} gold")

# How many more trades to afford an upgrade?
upgrade_cost = 500
trades_needed = upgrade_cost // gold_earned  # integer division — whole trades only
print(f"Trades needed for {upgrade_cost}g upgrade: {trades_needed}")

# In The Farmer Was Replaced, it looks like this:
#
# grass_held = num_items(Items.GRASS)
# if grass_held >= 10:
#     trade(Items.GRASS, 10)
