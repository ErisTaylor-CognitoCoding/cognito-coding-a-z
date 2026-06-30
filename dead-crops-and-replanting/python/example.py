# Clear the failure state before starting again
# Run this: python dead-crops-and-replanting/python/example.py

field = ["grass", "dead", "grass", "dead", "dead", "grass"]
resets = 0

for i, tile in enumerate(field):
    if tile == "dead":
        field[i] = "empty"   # till — clear the dead crop
        field[i] = "grass"   # replant
        resets += 1
        print(f"Tile {i}: cleared and replanted")
    else:
        print(f"Tile {i}: healthy — no action needed")

print(f"\nTotal resets: {resets}")

# In The Farmer Was Replaced, it looks like this:
#
# if get_entity_type() == Entities.DEAD:
#     till()
#     plant(Entities.GRASS)
#
# Try tracking what percentage of the field needed resetting.
