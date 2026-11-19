# 11.5 Practice: Line Joining

from math import sqrt
a = 1
b = -3
c = 2

# Implicit Joining - Preferred
x1 = ((-b + sqrt(b ** 2 - 4 * a * c))
      / (2 * a))
print("x1 =", x1)

# Explicit Joining - End the Line with a Backslash - NOTHING May Follow the Backslash, or Else SYNTAX ERROR
x2 = (-b - sqrt(b ** 2 - 4 * a * c)) \
     / (2 * a)
print("x2 =", x2)