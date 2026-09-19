
#Import the math library

import math

# Ask the user for the radius

radius =- int(input("Enter the radius of the garden in meters:"))

# Perform the required calculations

area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
areaSquareRoot = math.sqrt(area)
areaRoundedDown = math.floor(area)
areaRoundedUp = math.ceil(area)

# Display the results
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} square meters")
print(f"Square root of the area: {areaSquareRoot:.2f} square meters")
print(f"Area rounded down: {areaRoundedDown} square meters")
print(f"Area rounded up: {areaRoundedUp} square meters")