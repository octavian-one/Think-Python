import turtle
import math
bob = turtle.Turtle()
print(bob)

## My first attempts are below
def square(turtle, length):
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)

#square(bob, 250)

def polygon(turtle, length, n):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(360/n)
        

#polygon(bob, 250,5)


"""4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference."""

def circle(t, r):
    polygon(t, r, 360)

#circle(bob, 1)


"""Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle."""

def arc (t, r, angle):
      for i in range(angle):
        t.fd(r)
        t.lt(360/angle)

#arc(bob, 5, 20)


## Following through with book attempts are below:

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

#circle(bob, 50)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        #print (str(length) + ' ' + str(angle))

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
   
    polyline(t, n, step_length, step_angle)

bob.speed(0)

#arc(bob, 100, 9000)
""" pretty interesting flower
def leaf(turtle, length, leaves):
    for i in range(leaves*20):
        turtle.lt(360/leaves*2)
        arc(turtle, length, 100)
        turtle.lt(360/leaves*2)
        arc(turtle, length, 100)
   """    


""" Getting there
def leaf(turtle, length, leaves):
    for i in range(leaves):
        turtle.lt(10)
        arc(turtle, length, 100)
        turtle.lt(360/leaves)
        arc(turtle, length, 100)
leaf(bob, 100, 5)"""

"""def leaf(turtle, length, leaves):
    for i in range(leaves):
        #turtle.lt(360/leaves)
        arc(turtle, length, 100)
        turtle.rt(-270)
        arc(turtle, length, 100)
leaf(bob, 50, 4)
"""
turtle.mainloop()