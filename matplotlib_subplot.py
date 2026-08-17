# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np 

'''

Matplotlib Subplots

Overview:

Matplotlib subplots allow you to create a grid of subplots within a single figure. This is very useful when you need to display multiple plots in a
structured layout to compare them side by side or in a sequence.
. plt.subplots() function: This is the key function to create a figure and a set of subplots. It returns a tuple containing a Figure object and an
array of Axes opjects.

'''

# Basic Example of Using subplots():

# Create a figure and a single subplot
fig, ax = plt.subplots()

# Plot data
ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]) # Plotting squares of the numbers

# Show the plot
plt.show()



#Adding Rows and Columns of Subplots: You can specify the number of rows and columns of subplots in the plt.subplots() function.

#Creating a 2x2 grid of subplots:

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2) # 2 rows. 2 columns
# Plot data in each subplot
axs[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])    # Top-left
axs[0, 1].plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])      # Top-right
axs[1, 0].plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])      # Bottom-left
axs[1, 1].plot([1, 2, 3, 4, 5], [25, 16, 9, 4, 1])    # Bottom-right

# Show the plot
plt.show()




# Using plt.tight_layout():
# The plt.tight_layout() function is used to automatically adjust subplot parameters to give specified padding and avoid overlap between subplots.

# Example of plt.tight_layout():
# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Plot data
axs[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
axs[0, 1].plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
axs[1, 0].plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
axs[1, 1].plot([1, 2, 3, 4, 5], [25, 16, 9, 4, 1])

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()



'''

Experimenting with Subplot Parameters: You can adjust a multitude of parameters to customize the appearance and functionality of subplots.
Common Parameters:

. figsize: Tuple of width and height in inches to specify the size of the figure.
. dpi: Dots per inch, resolution of the figure.
. sharex, sharey: If set to True, subplots share the x or y axis.
. subplot_kw: Dictionary of keywords passed to the add_subplot() call used to create each subplot.

'''
# Create a grid of subplots with shared y-axis and custom size
fig, axs = plt.subplots(2, 2, figsize=(10, 8), dpi=100, sharey=True, subplot_kw={'facecolor': 'lightgray'})

# Plotting
axs[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
axs[0, 1].plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
axs[1, 0].plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
axs[1, 1].plot([1, 2, 3, 4, 5], [25, 16, 9, 4, 1])

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
