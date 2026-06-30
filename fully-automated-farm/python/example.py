# Composition — small pieces working together as one system
# Run this: python fully-automated-farm/python/example.py

field = ["dead", "grass", "grass", "dead", "grass"]
gold = 0
grass_held = 0

def clear_dead_tiles():
    cleared = 0
    for i, tile in enumerate(field):
        if tile == "dead":
            field[i] = "grass"
            cleared += 1
    return cleared

def harvest_all():
    global grass_held
    harvested = 0
    for tile in field:
        if tile == "grass":
            grass_held += 1
            harvested += 1
    return harvested

def sell_if_ready():
    global gold, grass_held
    if grass_held >= 5:
        gold += grass_held * 3
        print(f"  Sold {grass_held} grass for {grass_held * 3}g (total: {gold}g)")
        grass_held = 0

# One pass of the farm loop
print("--- Farm run ---")
cleared = clear_dead_tiles()
print(f"Cleared {cleared} dead tiles")

harvested = harvest_all()
print(f"Harvested {harvested} grass")

sell_if_ready()
print(f"Gold: {gold}  |  Grass in hand: {grass_held}")

# In The Farmer Was Replaced:
# while True:
#     clear_dead()
#     harvest_row()
#     sell_if_ready()
#     move(South)
