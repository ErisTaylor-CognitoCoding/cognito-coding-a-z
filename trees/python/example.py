# if / elif — one check, multiple outcomes
# Run this: python trees/python/example.py

tiles = ["tree", "bush", "empty", "tree", "mushroom", "empty"]

for tile in tiles:
    if tile == "tree":
        print("Harvesting wood 🪵")
    elif tile == "bush":
        print("Harvesting berries 🫐")
    elif tile == "empty":
        print("Planting a new tree 🌱")
    else:
        print(f"Unknown tile: {tile} — skipping")

# In The Farmer Was Replaced, it looks like this:
#
# entity = get_entity_type()
# if entity == Entities.TREE:
#     if can_harvest(): harvest()
# elif entity == Entities.BUSH:
#     harvest()
# elif entity == Entities.NONE:
#     plant(Entities.TREE)
#
# Try adding "mushroom" as a fourth case.
