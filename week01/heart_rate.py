"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("What is your age? "))

max = 220 - age

top = .85 * max
bottom = .65 * max

print(f"When exercising to strengthen your heart, you should keep your heart rate between {round(bottom)} and {round(top)} beats per minute.")