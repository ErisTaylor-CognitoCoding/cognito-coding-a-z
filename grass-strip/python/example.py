# For Loop — cover every item in one go
# Run this: python grass-strip/python/example.py

row_length = 5

for i in range(row_length):
    print(f"Harvesting tile {i}")

# In The Farmer Was Replaced, it looks like this:
#
# for i in range(get_world_size()):
#     harvest()
#     move(East)
#
# Try changing row_length to different values.
# The loop adjusts automatically — you never rewrite it.
