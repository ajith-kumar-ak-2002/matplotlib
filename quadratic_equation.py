# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# pyrefly: ignore [missing-import]
import numpy as np

# Qudratic equation typically has the form y=ax^2 + bx + c, Where a, b and c constants
    #Here's How you can plot the qudratic equation y = x^2 -4x +4 using numpy and Matplotlib

#Define the coefficients
a = 1
b = -4
c = 4

#Generate x values
x = np.linspace(-1, 7, 400)

#Calculate Y value using the quadratic equation y=ax^2 + bx + c
y = a*(x**2) + b*x + c  

#Create the plot
plt.plot(x,y, label='y = x^2 -4x + 4')

#adding title and Label 
plt.title('Plot of the Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')

#add grid
plt.grid(True)

#show the plot
plt.show()


