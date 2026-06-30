# While True — a loop that never stops
# Run this: python harvest/python/example.py
# Press Ctrl+C to stop it

counter = 0

while True:
    counter = counter + 1
    print(f"Harvest #{counter}")

    # Uncomment these lines to make it stop after 5:
    # if counter >= 5:
    #     break

# In The Farmer Was Replaced, it looks like this:
#
# while True:
#     harvest()
#
# The drone keeps going until the game ends.
