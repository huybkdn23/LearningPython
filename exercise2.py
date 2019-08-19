from turtle import Turtle, Screen
import math
bob = Turtle(shape="turtle")
print(bob)
def square(t, distance):
    for i in range(4):
        t.forward(distance)
        t.left(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

# bob._delay(0.01)
bob.penup()
radius = 250
square(bob, radius)
bob.rt(90)
bob.fd(150)
bob.rt(90)
bob.fd(30)
bob.rt(180)
bob.pendown()
bob._delay(0.01)
circle(bob, radius)
bob.penup()
# bob._delay(30)
# polygon(bob, 7, 250)
screen = Screen()
screen.exitonclick()
# bob = Turtle()
# print(bob)
# a = input("press")