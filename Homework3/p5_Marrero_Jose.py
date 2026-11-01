import turtle

def draw_leaf_straight(level, stem_length):
    turtle.left(90)
    turtle.forward(stem_length / 2)

    if level > 0:
        branch(level, stem_length / 2)

    turtle.forward(stem_length / 2)  


def branch(level, length):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    if level > 0:
        # Move forward
        turtle.forward(length)

        # Turn left
        turtle.left(30)

        # Draw left recursive branch
        branch(level - 1, length * 0.7)

        # Restore direction
        turtle.right(30)

        # Turn right
        turtle.right(30)

        # Draw right recursive branch
        branch(level - 1, length * 0.7)

        # Restore direction
        turtle.left(30)

        # Move backward
        turtle.backward(length)
# Test Figure 1(b)
draw_leaf_straight(2, 120)
turtle.done()