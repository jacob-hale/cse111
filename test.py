from datetime import datetime

day = datetime.now() 

subtotal = float(input("Please enter subtotal: "))

tax = float(subtotal * 0.06)

if (day.strftime("%w") == 2 or day.strftime("%w") == 3) and subtotal >= 50:
    total = (subtotal * .9) + tax
    discount = total - subtotal
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Discount amount: {discount:.2f}")
    print(f"Total: {total:.2f}")
else:
    total = subtotal + tax 
    print(f"Sales tax amount: {tax:.2f}")
    print(f"Total: {total:.2f}")