def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Display the final price or the original price
if final_price == original_price:
    print(
        f"No discount applied. The original price is: {original_price}"
    )
else:
    print(
        f"The final price after applying the discount is: {final_price}"
    )
