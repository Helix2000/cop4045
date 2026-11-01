import turtle
# Jose Marrero Z Number: Z23816617
def draw_leaf_straight(level: int, stem_length: float) -> None:
    """draws leaf using recursive branching"""
    turtle.left(90)
    turtle.forward(stem_length / 2)
    branch(level, stem_length / 2)
    turtle.forward(stem_length / 2)
    

def branch(level: int, stem_length: float) -> None:
    """draws small branches of the leaf"""
    
    if level == 0:
        return
    turtle.forward(stem_length)
    turtle.left(30)
    branch(level - 1, stem_length * 0.7)
    
    turtle.right(30)
    turtle.right(30)
    branch(level - 1, stem_length * 0.7)
    turtle.left(30)
    turtle.backward(stem_length)


draw_leaf_straight(6, 120)
turtle.hideturtle()
turtle.done()
