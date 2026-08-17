# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np 

# Creating and Plotting a Linear Equation and a Quadratic Equation with NumPy and Matplotlib?
# A linear equation in two variables (say, x and y) can be represented as y = mx + c, where m is the slope of the line, and c is the y-intercept. Let's plot a simple linear equation using Matplotlib and NumPy.


# 1. Create an array for x values: Use NumPy to create an array of x values from which y values will be calculated.
x = np.linspace(start = -10 , stop = 10, num = 400)


# 2. Define the linear equation: Specify the slope (m) and intercept (c).
m = 2    #Slope
c = 3    #intercept
y = m * x + c 

# 3. Plot the equation: Use Matplotlib to plot the line.

plt.plot(x, y , label= 'y = 2x + 3')
plt.title('Plot of the Linear Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,10)
plt.ylim(0,20)
plt.grid(True)
plt.legend()
plt.show()
plt.savefig('Linear-Equation.png')

'''
In this code:

. np.linspace(start, stop, num) generates num evenly spaced samples, calculated over the interval [start, stop].
. plt.plot(x, y, label) plots y versus x as lines and/or markers with an optional label.
. plt.title(), plt.xlabel(), and plt.ylabel() are used to add a title and labels to the axes.
. plt.grid(True) enables a grid to make reading the plot easier.
. plt.savefig() allows you to save the figure in various file formats such as PNG, JPEG, SVG, PDF, and more.
. plt.show() displays the plot.
This will produce a graph of the linear equation y = 2x + 3, showing a straight line that cuts through the y-axis at 3 and has a slope of 2, rising
two units in y for every increase of one unit in x.

A quadratic equation typically has the form y = ax^2 + bx + c, where a, b and c are constants.
Here's how you can plot the quadratic equation y = x^2 - 4x + 4:

'''

