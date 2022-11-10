import math

items = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

def compute_box(items, per_box):
    return math.ceil(items / per_box)

print(f"For {items} items, packing {per_box} items in each box, you will need {compute_box(items, per_box)} boxes.")