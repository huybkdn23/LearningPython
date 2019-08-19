from turtle import Turtle, Screen
import math

def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        t.fd(n)
        return
    m = n/3.0
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = Turtle(shape="turtle")
bob._delay(0.0001)

bob.x = -150
bob.y = 90

snowflake(bob, 300)
screen = Screen()
screen.exitonclick()