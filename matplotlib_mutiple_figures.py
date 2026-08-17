# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np


'''

v Creating a Matplotlib Figure with Multiple Axes Arranged at Various Positions

Overview:

When creating visualizations in Matplotlib, the figure serves as a canvas where multiple plots (axes) can be arranged in various positions. Ead
set of axes can display different aspects or components of data. For linear functions, these plots might represent different linear equations o
variations thereof.

Key Components:

. Figure: The entire window or the canvas for the plots.
. Axes: The individual plots; each set of axes can contain its own elements like lines, labels, ticks, and titles.

Configuring Multiple Axes:
To position axes, use fig.add_axes() with the format [left, bottom, width, height] where each value is a fraction of the figure dimensions:
. left, bottom: These determine the position of the bottom-left corner of the axes.
. width, height: These determine the size of the axes.
Example Code for Linear Functions in Different Axes Positions:

This example demonstrates how to arrange six different axes within a single figure, each displaying a simple linear function with a difference 
slope and intercept, organized in various Positions.

'''

# Generate x values
x = np. linspace(0, 10, 100)

# Create a blank canvas
fig = plt.figure(figsize=(10,8))


# Center plot - main plot
axes_center = fig.add_axes([0.3, 0.3, 0.4, 0.4]) # left, bottom, width, height
axes_center.plot(x, x +1) # y = x +1
axes_center.set_title('Center Plot: y = x + 1')

# Top plot - summary
axes_top = fig.add_axes([0.3, 0.75, 0.4, 0.2])
axes_top.plot(x, 2*x + 1) # y = 2x + 1
axes_top.set_title('Top Plot: y = 2x + 1')

# Right plot - auxiliary data
axes_right = fig.add_axes([0.75, 0.3, 0.2, 0.4])
axes_right.plot(x, 0.5*x + 1) # y = 0.5x + 1
axes_right.set_title('Right Plot: y = 0.5x + 1')

# Left plot - contextual information
axes_left = fig.add_axes([0.05, 0.3, 0.2, 0.4])
axes_left.plot(x, 3*x + 1) # y = 3x + 1
axes_left.set_title('Left Plot: y = 3x + 1')

# Bottom plot - comparative data
axes_bottom = fig.add_axes([0.3, 0.05, 0.4, 0.2])
axes_bottom.plot(x, -x + 1) # y = -x + 1
axes_bottom.set_title('Bottom Plot: y = -x + 1')

# Top Right Corner plot - highlight
axes_top_right = fig.add_axes([0.75, 0.75, 0.2, 0.2])
axes_top_right.plot(x, 4*x + 1) # y = 4x + 1
axes_top_right.set_title('Top Right Plot: y = 4x + 1')

plt.show()