# 27.1
INCH = 25.4     # millimeters in an inch
WIDTH = 8.5     # inches of a paper
HEIGHT = 11     # inches of a paper
milW = INCH * WIDTH
milH = INCH * HEIGHT
milW = round(milW, 1)
milH = round(milH, 1)
print("A letter-size paper is", milW, "millimeters wide and", milH, "millimeters tall.")
# 27.2
perim = 2 * (WIDTH + HEIGHT)
sqW = WIDTH * WIDTH
sqH = HEIGHT * HEIGHT
sqdiagonal = sqW + sqH
diagonal = sqdiagonal ** 0.5
diagonal = round(diagonal, 1)
print("The perimeter of a letter-size paper is", perim, "inches, and the diagonal length of is", diagonal, "inches.")
# 27.3
num = input("Enter a number: ")
num = int(num)
numsq = num ** 2
numcube = numsq * num
numquart = numsq ** 2
print(num, numsq, numcube, numquart)