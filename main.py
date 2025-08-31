import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

#Make it a safe expression using numpys built-in tools
def safe_eval(expression, X, Y):
    allow_global = {"np": np}
    allow_vars = {"x" : X, "y": Y}
    return eval(expression, allow_global, allow_vars)

#This creates the differential equation and plots the slope
def direction_field(x, y, equation):
    #creating the meshgrid
    x = np.arange(-x, x, 0.5) 
    y = np.arange(-y, y, 0.5) 
    X, Y = np.meshgrid(x,y)

    #Evaluates the expression
    dy = safe_eval(equation, X, Y)
    dx = np.ones_like(dy)

    #Making the each arrow color change depending on the slope
    C = dy
    cmap = "seismic"
    vmax = np.nanmax(np.abs(C))
    norm_c = TwoSlopeNorm(vmin=-vmax, vcenter=0.0, vmax=vmax) if vmax > 0 else None

    #Normalizing 
    norm = np.hypot(dy, dx)
    norm[norm == 0] = 1.0
    dyu = dy/norm
    dxu = dx/norm
    
    #Plotting the arrows
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_facecolor("gray")
    q = ax.quiver(X, Y, dxu, dyu, C, cmap = cmap, norm = norm_c, pivot="mid", angles="xy", scale_units="xy")
    fig.colorbar(q)

    ax.axhline(0, color="white", linewidth=0.5, alpha=0.5)
    ax.axvline(0, color="white", linewidth=0.5, alpha=0.5)

    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Direction Field for y'= " + equation)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(False)
    plt.show()



#Collecting the differential equation, can use numpy too
print("Enter your Differential Equation('x - y', 'x**2 - y')")
equation = input("y' = ")

print("\nEnter x-grid")
x_coord = input("[-input, +input]: ")

print("\nEnter y-grid")
y_coord = input("[-input, +input]: ")

direction_field(int(x_coord), int(y_coord), equation)
