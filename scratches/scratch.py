from turtle import *

shape("turtle")
speed(0)

def tree(size, levels, angle):
    if levels == 0:
        return

    forward(size)
    right(angle)

    tree(size * 0.85, levels -1, angle)

    left(angle * 2)

    tree(size * 0.85, levels -1, angle)

    right(angle)
    backward(size)


tree(90, 8, 60)


mainloop()
