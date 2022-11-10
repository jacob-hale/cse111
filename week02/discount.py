from datetime import datetime
price = 1
subtotal = 0
day = datetime.now() 
while price != 0:
    price = float(input("Please enter product price: "))
    if price != 0:
        quantity = float(input("Please enter the quantity: "))
        subtotal += price * quantity
if (day.strftime("%w") == 2 or 3) and subtotal >= 50:
    total = (subtotal * .9)
    discount = subtotal - total
    tax = float(total * 0.06)
    total_new = total + tax
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Discount amount: {discount:.2f}")
    print(f"Total: {total_new:.2f}")
else:
    tax = float(subtotal * 0.06)
    total = subtotal + tax 
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {total:.2f}")