# Patience — wait until the condition is true before acting
# Run this: python cactus-patience/python/example.py

min_age = 5
items = [
    {"name": "Cactus A", "age": 3},
    {"name": "Cactus B", "age": 7},
    {"name": "Cactus C", "age": 5},
    {"name": "Cactus D", "age": 1},
]

for item in items:
    if item["age"] >= min_age:
        print(f"{item['name']}: ready — harvesting ✅")
    else:
        print(f"{item['name']}: not ready (age {item['age']}) — skipping ⏳")

# In The Farmer Was Replaced, it looks like this:
#
# if get_entity_type() == Entities.CACTUS:
#     if can_harvest():
#         harvest()
#     else:
#         move(North)  # skip and revisit
#
# Try changing min_age and see which cacti get harvested.
