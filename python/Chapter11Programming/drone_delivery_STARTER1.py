#  Plans drone delivery trips from a warehouse to a customer and reports
#  the straight-line distance, number of trips, total distance flown,
#  and total time (flying + loading).
#
#  PART A - HAND CALCULATION  (3 km east, 4 km north, 40 km/h, 7 packages, 2 per trip)
# east = 3
# north = 4
# line = math.sqrt((3 ** 2) + (4 ** 2)) = sqrt(9 + 16) = 5
# speed = 40
# packages = 7
# numCarry = 2
# trips = math.ceil(packages / numCarry) = 4
# tripTime = 2 * (line / speed) = 2 * 0.125 = 0.25 hr/trip
# totalTime = trips * tripTime = 1.75 hrs
# totalDis = (line * 2) * trips = 70 miles
#
#  Import style: "import math" - writing math.sqrt and math.ceil makes it
#  clear to any reader which module each function comes from.
import math
yDis = float(input("Y Distance: "))
xDis = float(input("X Distance: "))
speed = float(input("Drone speed: "))
packages = float(input("Number of packages: "))
CARRY = 2
line = math.sqrt((xDis ** 2) + (yDis ** 2))
trips = math.ceil(packages / CARRY)
tripTime = 2 * (line / speed)
totalTime = trips * tripTime
totalDis = (line * 2) * trips
print("Distance to customer:", line, "miles")
print("Number of trips:", trips,)
print("Total distance flown:", totalDis, "miles")
print("Total time:", totalTime, "hours")