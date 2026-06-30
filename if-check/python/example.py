# If Check — making decisions in code
# Run this: python if-check/python/example.py

score = 15

if score >= 10:
    print("Harvest — it's ready!")
else:
    print("Not ready — move on.")

# In The Farmer Was Replaced, it looks like this:
#
# while True:
#     if can_harvest():
#         harvest()
#     else:
#         move(North)
#
# Try changing 10 to different values and watch the output change.
