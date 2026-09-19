# Project title: calculating information about a garden based on its radius
# Description: This program asks for the radius and calculates the area, circumference, quare root of the calculated area, area rounded down, and the area rounded up of the garden.


# Import the math library
import math

# Ask the user for the radius(input)

radius =- int(input("Enter the radius of the garden in meters:"))


# Perform the required calculations


area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
areaSquareRoot = math.sqrt(area)
areaRoundedDown = math.floor(area)
areaRoundedUp = math.ceil(area)


# Display the results(output)

print(f"Area of the garden: {area:.2f}, square meters")
print(f"Circumference of the garden: {circumference:.2f}, square meters")
print(f"Square root of the area: {areaSquareRoot:.2f} , square meters")
print(f"Area rounded down: {areaRoundedDown}, square meters")
print(f"Area rounded up: {areaRoundedUp}, square meters")


#  Computational Thinking
## Problem identification: Calculate the area, circumference, square root of the calculated area, area rounded down, and the area rounded up of the garden.
## Problem decomposition: I asked the radius using inputs, then used math libraries to calculate, and used output to display the results.
## Pattern recognition: I realized that the formulas are quite similar to each other, and they all need the use of math libraries.
## Data representation: They are represented by numbers
## Algorithm Development: 

# Author: Arrhiana Kei M. Villareal
# 