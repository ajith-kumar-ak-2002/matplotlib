# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np  


'''

In Matplotlib, the Figure object is a central concept. It acts as the container that holds everything you see on the plot, as well as the space in
which elements that make up the plot are drawn. Think of the Figure object as a canvas on which various plots are drawn.

Key Characteristics:
    . Container: It holds all plot elements, such as axes, graphics, text, and labels.
    . Independence: You can create multiple figures. Each figure can contain multiple Axes.
    · Customizable: Its size, DPI (dots per inch), and other attributes can be adjusted according to user needs.

v Creating a Figure
    When you create a figure in Matplotlib, you're setting up a space where plots will reside. Here's how you typically create a figure and add axes to it:

'''

#create a figure object
fig = plt.figure()

#add axes to the figure (left , bottom , width , height )
ax = fig.add_axes([0.1,0.1,0.8,0.8])

#Display Figure 
plt.show()


# Detail Explained

# Creating an array of x values
x = np.linspace(0, 10, 100)
# Calculating y values based on x
y = np.sin(x)

# Create a new figure with a specific size
fig = plt.figure(figsize=(8, 6))

# Add an axes to the figure
# The list [left, bottom, width, height] defines the dimensions of the axes within the figure
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])

# Plot data on the axes
ax.plot(x, y, label='sin(x)', color='blue')

# Set the title of the plot
ax.set_title('Simple Plot of sin(x)')

# Set the x and y axis labels
ax.set_xlabel('x')
ax.set_ylabel('Amplitude')

# Display the figure
plt.show()


'''

Breakdown:

1. Figure and Axes Creation: A Figure object is created with a specified size using figsize=(8,6). An Axes object is then added to this figure.
The list [0.1, 0.1, 0.85, 0.85] specifies the position and dimensions of the axes within the figure.
2. Plotting Data: np.sin(x) computes the sine of each value in x, and these points are plotted as a blue line.
3. Customization: The plot is dustomized with titles, labels, and a legend, which help in understanding the plotted data.

'''