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
# = means "is set to"
lives = 3
print("Lives at start:", lives, "lives.")
lives = lives + 2       # adding 2 lives to the total
print("After a power-up:", lives, "lives.")