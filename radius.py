#Jacob Jensen
#9/17/18
import math
#get name function
def get_name(name_input):
    

    name = name_input
    name = name.lower()
    name = name.title()
    
#display name
    print("The name you entered was", name)


print("This is our function")
name = input("What is your name? ")
get_name(name)


#area of a circle
def area_of_circle(radius1):
    PI = 3.14159265
    
#1 get a radius
    radius = radius1
    radius = float(radius)

#2 compute an area
    area = radius*radius*PI
    
#3 display information
    print("The area of the circle is: ", area)

radiusx = input("what is the radus")
area_of_circle(radiusx)

def pythagoras_theorum(ap, bp):

#a^2+b^2=c^2
    a = float(ap)
    b = float(bp)
    c = a*a + b*b
    c = math.sqrt(c)
    print("the third side is ",c)

ax = input("enter the first side of the triangle")
bx = input("enter the second line of the triangle")
pythagoras_theorum(ax, bx)


def add_number(x=0, y=0):
    num1 = x
    num2 = y
    num3 = int(num1) + int(num2)
    print(num1, "this is num1")
    print(num2, "this is num2")
    return num3

x=input("enter a number")
y=input("enter a second number")
num4= add_number(y,x)
print("the sum of your numbers is ")
print(num4)
