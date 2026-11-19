# 11.4 Practice: Combining Assignment and Arithmetic
# Each Shortcut Operator Updates a Variable Using its Current Value

# Basic
total = 10
cans = 4
total += cans
print("total += cans -->", total)       # 14
total *= 2
print("total *= 2 -->", total)      # 28

# Count by one
count = 0
count += 1
count += 1
count += 1
count += 1
count += 1
count += 1
print("count =", count)         # 6

# Realisitc Use: A Running Total (shopping cart)
cartTotal = 0
cartTotal += 3.49
cartTotal += 12.99
cartTotal += 1.25
print("Your cart total today is: $", str(round(cartTotal, 2)))