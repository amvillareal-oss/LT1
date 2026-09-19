
#Import the math library

import math

# Ask the user for the radius

radius = int(input("Enter the radius of the garden in meters:"))

# Perform the required calculations

## Calculate the area
area = math.pi * math.pow(radius, 2)
## Calculate the circumference
circumference = 2 * math.pi * radius
## Calculate the square root
areaSquareRoot = math.sqrt(area)
## Calculate rounded up
areaRoundedDown = math.floor(area)
## Calculate rounded up
areaRoundedUp = math.ceil(area)

# Display the results
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {areaSquareRoot:.2f} ")
print(f"Area rounded down: {areaRoundedDown} square meters")
print(f"Area rounded up: {areaRoundedUp} square meters")
