# Lists — a row of slots, all in one container

eggs = ["brown", "white", "speckled"]

print(eggs[0])    # brown  — slot 0 is the first one
print(eggs[1])    # white
print(eggs[2])    # speckled
print(len(eggs))  # 3 — how many slots are filled

# Loop through every item
for egg in eggs:
    print("Egg:", egg)
