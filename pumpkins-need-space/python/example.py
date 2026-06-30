# Read state before acting — don't assume, check
# Run this: python pumpkins-need-space/python/example.py

tiles = ["empty", "occupied", "empty", "occupied", "empty"]

for tile in tiles:
    if tile == "empty":
        print("Planting pumpkin 🎃")
    else:
        print("Tile busy — skipping")

# In The Farmer Was Replaced, it looks like this:
#
# if get_entity_type() == Entities.NONE:
#     plant(Entities.PUMPKIN)
#
# Try adding "blocked" as a third tile state and handle it with elif.
