# Running maximum — track the biggest value as you go
# Run this: python sunflowers-and-the-tallest-check/python/example.py

heights = [3, 7, 2, 9, 4, 1, 8]

tallest = 0

for h in heights:
    if h > tallest:
        tallest = h
        print(f"New tallest: {h}")

print(f"\nFinal answer: {tallest}")

# In The Farmer Was Replaced, it looks like this:
#
# tallest = 0
# for x in range(get_world_size()):
#     h = measure(Entities.SUNFLOWER)
#     if h > tallest:
#         tallest = h
#     move(East)
#
# Try finding the *smallest* value — what one thing changes?
