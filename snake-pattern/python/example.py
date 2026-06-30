# Nested Loops — cover every tile in a grid
# Run this: python snake-pattern/python/example.py

ROWS = 3
COLS = 3

for row in range(ROWS):
    for col in range(COLS):
        print(f"({row},{col})", end=" ")
    print()  # new line after each row

# In The Farmer Was Replaced, it looks like this:
#
# for y in range(get_world_size()):
#     for x in range(get_world_size()):
#         harvest()
#         if x < get_world_size() - 1:
#             move(East)
#     move(South)
#
# Try changing ROWS and COLS — the loops adjust automatically.
