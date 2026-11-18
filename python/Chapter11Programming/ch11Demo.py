# Variables, Airthmetic, and Importing Modules
# Demo 1 - variables and assignment
def demo1_variables():
    CAN_VOL = 0.355     # In liters
    BOTTLE_VOL = 2.0    # In liters
    cansPerPack = 6
    packVol = cansPerPack * CAN_VOL
    print("Six-pack volume:", packVol, "liters.")
    print("Bottle volume", BOTTLE_VOL, "liters.")
demo1_variables()
lives = 3
print("\nLives at start:", lives, "lives.")
lives = lives + 2       # adding 2 lives to the total
print("After a power-up:", lives, "lives.")
# Tuesday Practice
redTeam = 12
blueTeam = 30
redTeam, blueTeam = blueTeam, redTeam
print("\nRed:", redTeam, "Blue:", blueTeam)
# PEMDAS
print("\nOperators and Precidence:")
def demo3_operators():
    a = 10
    b = 4
    print("a + b / 2 =", a + b / 2)         # 12.0
    print("(a + b) / 2 =", (a + b) / 2)     # 7.0
    print("10 - 2 - 3 =", 10 - 2 - 3)       # 5
    print("7 + 4.0 =", 7 + 4.0)             # 11.0
    print("10 * 2 ** 3 =", 10 * 2 ** 3)     # 80
    print("2 ** 3 ** 2 =", 2 ** 3 ** 2)     # 512
demo3_operators()
# Compound Interest: balance * (1 + rate / 100) ** years
balance = 1000
rate = 5.0
years = 10
future = balance * (1 + rate / 100) ** years
print("\nFuture Value:", round(future, 2))
# Division
print("\nFloor Division and Modulus")
def demo4_floor_mod():
    print("17 / 5 =", 17 / 5)               # 3.4
    print("17 // 5 =", 17 // 5)             # 3
    print("17 % 5 =", 17 % 5)               # 2
demo4_floor_mod()
# Practice
screenMinutes = 437
HR = 60
hours = screenMinutes // HR
minutes = screenMinutes % HR
print("")
print(hours, "hours and", minutes, "minutes.")
# Convert a video length in seconds to minutes and seconds
videoSeconds = 754
MIN = 60
minutes = videoSeconds // MIN
seconds = videoSeconds % MIN
print("Video length:", minutes, "minutes and", seconds, "sec.")
n = 2026
print("\nLast Digit:", n % 10)
print("Without last digit:", n // 10)
print("Even? Remainder is:", n % 2)
# Demo 5
print("\nDEMO 5 - Built-in Functions, the Math module, roundoff")
def demo5_functions():
    from math import sqrt, pi
    print("abs(-42) =", abs(-42))                                   # 42 Built-in
    print("round(3.14159) =", round(3.14159))                       #3 Built-in
    print("round(3.14159, 3) =", round(3.14159, 3))                 # 3.142 Built-in
    print("max(52, 64, 37, 89, 34) =", max(52, 64, 37, 89, 34))     # 89 Built-in
    print("min(52, 64, 37, 89, 34) =", min(52, 64, 37, 89, 34))     # 34 Built-in
    # math module functions
    a = 3
    b = 4
    c = sqrt((a ** 2) + (b ** 2))
    print("\nHypotenuse:", c)                 # 5.0
    print("Find the area of a circle:")
    radius = 2.5
    area = pi * radius ** 2
    print("Circle area:", round(area, 2))
    print("Roundoff error: binary can't store 4.35 exactly")
    price = 4.35
    quantity = 100
    total = price * quantity
    print("Total:", total)
demo5_functions()
# Import
from math import sqrt, pi
radius = sqrt(50)
print("")
print(round(pi * radius ** 2, 2))
# import math
# radius = math.sqrt(50)
# print(round(math.pi * radius ** 2, 2))
# from math import *
# radius = sqrt(50)
# print(round(pi * radius ** 2, 2))