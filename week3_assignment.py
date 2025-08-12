def calculate_discount(price, discount_percent):
    """
    Return the final price after applying the discount only if
    discount_percent is 20% or higher. Otherwise return the original price.
    """
    if discount_percent >= 20:
        return round(price * (1 - discount_percent / 100), 2)
    return round(price, 2)


# --- Program starts here ---
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

if price < 0:
    print("Price cannot be negative.")
    exit()
if discount_percent < 0 or discount_percent > 100:
    print("Discount percentage must be between 0 and 100.")
    exit()

final_price = calculate_discount(price, discount_percent)

if final_price < price:
    print(f"Discount applied ({discount_percent}%). Final price: {final_price}")
else:
    print(f"No discount applied (discount < 20%). Price remains: {price}")