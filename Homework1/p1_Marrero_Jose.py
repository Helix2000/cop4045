import math
import matplotlib.pyplot as plt
import numpy as np

while True:
    a = input("Enter a value for 'a': ")
    if a == "":
        break
    a = float(a)

    b = input("Enter a value for 'b': ")
    b = float(b)

    c = input("Enter a value for 'c': ")
    c = float(c)

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("no real solutions")
    elif discriminant == 0:
        x1 = -b / (2*a)
        print("one solution: x =", x1)
    else:
         
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("two solutions: x1 =", x1, ", x2 =", x2)

    if discriminant < 0:
        xopt = -b / (2*a)
        x = np.linspace( xopt -10, xopt + 10, 150)
        y = a * x**2 + b * x + c
        plt.plot(x, y)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.title("Quadratic Function: No Real Solutions")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()

    elif discriminant == 0:
        xopt = x1
        x = np.linspace( xopt -10, xopt + 10, 150)
        y = a * x**2 + b * x + c
        plt.plot(x, y)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.title("Quadratic Function: One Real Solution")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()

    else:
        smaller_root = min(x1, x2)
        larger_root = max(x1, x2)

        start = smaller_root - 2
        end = larger_root + 2

        x = np.linspace(start, end, 150)
        y = a * x**2 + b * x + c
        plt.plot(x, y)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.title("Quadratic Function: Two Real Solutions")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()

        