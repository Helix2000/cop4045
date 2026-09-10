import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    x_min, x_max = domain

    xs = []
    ys = []

    step = (x_max - x_min) / (ns - 1)  
    for i in range(ns):
        x = x_min + i * step
        xs.append(x)

    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    print("x", "y")
    for i in range(ns):
        print("{:.4f} {:.4f}".format(xs[i], ys[i]))

    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of {}".format(fun_str))
    plt.show()  

fun_str = input("Enter x function:")
ns = int(input("Enter sample number:"))

x_min = float(input("Enter x min:"))
x_max = float(input("Enter x max:"))
domain = (x_min, x_max)

plot_function(fun_str, domain, ns)

