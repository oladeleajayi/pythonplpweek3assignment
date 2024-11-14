# Question 1
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

original_price = 100
discount = 25
final_price = calculate_discount(original_price, discount)
print(final_price)  # Output will be 75.0

original_price = 100
discount = 10
final_price = calculate_discount(original_price, discount)
print(final_price)  # Output will be 100.0 (no discount applied)



# Question 2
# Using the calculate_discount function, prompt the user to enter the original price of an item 
# and the discount percentage. Print the final price after applying the discount, 
# or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")

#  code output
# Enter the original price of the item: 100
# Enter the discount percentage: 25
# The final price after applying the discount is: $75.00


# Enter the original price of the item: 100
# Enter the discount percentage: 10
# No discount applied. The original price is: $100.00
