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