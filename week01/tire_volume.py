import math
from datetime import datetime

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print()
volumes = []
now = datetime.now()
date = now.strftime("%Y-%m-%d")


def compute_volume(w, a, d):
    return ((math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000)
        
v =  compute_volume(w, a, d)

print(f"The approximate volume is {compute_volume(w, a, d):.2f} liters")
price = ((.25 * w) + .5 * a + d)
print(f"Price per tire: ${price:.2f}")
buy = input("Do you want to purchase tires of those dimensions? (Yes/No) ") 
if buy.lower() == "yes":
    phone = input("Please enter your phone number: ")
    new = [date, w, a, d, float(f"{v:.2f}"), phone, price]
else:
    print("No worries, have a great day!")
    new = [date, w, a, d, float(f"{v:.2f}")]

with open("volumes.txt", mode = "at") as volumes_file:
    volumes.append(new)
    print(volumes, file = volumes_file)