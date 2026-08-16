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