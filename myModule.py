from math import pi

def sqFootage(length, width):
    squareFootage = length * width
    return squareFootage

def circleCircumference(radius):
    circumference = 2*(pi)*radius
    return circumference

def formatUser(aString):
    return aString.strip().title()

print(formatUser("      gDsss  "))
print(sqFootage(500, 600))
print(circleCircumference(30))