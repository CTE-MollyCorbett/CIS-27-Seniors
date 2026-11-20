#  Section 11.7 Worked Example: Computing Travel Time
#  A robot drives along a road (fast), then cuts straight across rocky
#  terrain (slow) to reach an item. Compute the total travel time.
#
#  HAND CALCULATION (dx(segment 2 base length) = 4 m, dy(segment 2 height) = 3 m, l1(segment length 1) = 6 m,
#  s1(segment 1 speed) = 5 mph, s2(segment 2 speed) = 2 mph):
#    Segment 1 time   = 6 / 5 = 1.2 hr
#    Segment 2 length = sqrt(4 ** 2 + 3 ** 2) = sqrt(16 + 9) = sqrt(25) = 5
#    Segment 2 time   = 5 / 2 = 2.5 hr
#    Total time       = 3.7 hr
#
from math import sqrt
seg1length = float(input("Segment 1 distance: "))
seg1speed = float(input("Speed (in miles) along Segment 1: "))
baseDist = float(input("Base distance of Segment 2: "))
height = float(input("Height distance of Segment 2: "))
seg2speed = float(input("Speed (in miles) along Segment 2: "))
seg1time = seg1length / seg1speed
seg2length = sqrt((baseDist ** 2) + (height ** 2))
seg2time = seg2length / seg2speed
totalTime = round(seg1time + seg2time, 2)
print("Total time:", totalTime, "hours.")

# ---------------------------------------------------------------
# TRY IT
#  1. Run with 4, 3, 6, 5, 2.  Does the program match the hand value 3.7?
#  2. By hand: what if the robot drives 8 km on the road instead of 6?
#     (Hint: segment 2 becomes a 2-3 right triangle.) Then check it.
#  3. Rewrite the import as "import math". What else must change?
# ---------------------------------------------------------------
# This was unnecessarily confusing.