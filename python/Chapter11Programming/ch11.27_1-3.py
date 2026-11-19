# 27.1 Write a program that displays the dimensions of a letter-size
# (8.5 × 11 inch) sheet of paper in millimeters.
# There are 25.4 millimeters per inch.
# Use constants and comments in your program.
INCH = 25.4     # millimeters in an inch
WIDTH = 8.5     # inches of a paper
HEIGHT = 11     # inches of a paper
milW = INCH * WIDTH
milH = INCH * HEIGHT
milW = round(milW, 1)
milH = round(milH, 1)
print("A letter-size paper is", milW, "millimeters wide and", milH, "millimeters tall.")

# 27.2 Write a program that computes and displays the perimeter
# of a letter-size (8.5 × 11 inch) sheet of paper and the length of its diagonal.
perim = 2 * (WIDTH + HEIGHT)
sqW = WIDTH * WIDTH
sqH = HEIGHT * HEIGHT
sqdiagonal = sqW + sqH
diagonal = sqdiagonal ** 0.5
diagonal = round(diagonal, 1)
print("The perimeter of a letter-size paper is", perim, "inches, and the diagonal length of is", diagonal, "inches.")

# 27.3 Write a program that reads a number and displays the square, cube, and fourth power.
# Use the ** operator only for the fourth power.
num = input("Enter a number: ")
num = int(num)
numsq = num ** 2
numcube = numsq * num
numquart = numsq ** 2
print(num, numsq, numcube, numquart)