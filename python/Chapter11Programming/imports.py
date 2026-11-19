# 11.3 Practice: Other Ways to Import Modules

# Import Specific Functions By Name
from math import sqrt, ceil, floor
print("Style 1: from math import sqrt, ceil, floor")
print("sqrt(81) =", sqrt(81))
print("ceil(4.2) =", ceil(4.2))         # Upper rounding
print("floor(4.8) =", floor(4.8))       # Lower rounding

# Import the Whole Module, then Use module.function
import math
print("\nStyle 2: import math")
print("math.sqrt(81) =", math.sqrt(81))
print("math.pi =", math.pi)
print("math.pow(2, 5) =", math.pow(2, 5))

# Import Everthing With *
from math import *
print("\nStyle 3: from math import *")
print("cos(0) =", cos(0))
print("e =", e)
e = 5                   # Name collision - overwrite a variable that already exists
print("e =", e)