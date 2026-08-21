# Python Matplotlib Tutorial & Reference Guide

Welcome to the **Python Matplotlib** learning journey! This repository is organized as a structured tutorial following the learning path shown below. Each section features a detailed explanation and runnable Python examples.

---

## 🗺️ Learning Path

* [Matplotlib Intro](#1-matplotlib-intro)
* [Matplotlib Get Started](#2-matplotlib-get-started)
* [Matplotlib Pyplot](#3-matplotlib-pyplot)
* [Matplotlib Plotting](#4-matplotlib-plotting)
* [Matplotlib Markers](#5-matplotlib-markers)
* [Matplotlib Line](#6-matplotlib-line)
* [Matplotlib Labels](#7-matplotlib-labels)
* [Matplotlib Grid](#8-matplotlib-grid)
* [Matplotlib Subplot](#9-matplotlib-subplot)
* [Matplotlib Scatter](#10-matplotlib-scatter)
* [Matplotlib Bars](#11-matplotlib-bars)
* [Matplotlib Histograms](#12-matplotlib-histograms)
* [Matplotlib Pie Charts](#13-matplotlib-pie-charts)

---

## 1. Matplotlib Intro

**Matplotlib** is a low-level graph plotting library in Python that serves as a visualization utility. It was created by John D. Hunter and is open-source.

### Key Capabilities
* **Interactive Figures:** Zoom, pan, and update plots dynamically.
* **Highly Customizable:** Adjust line styles, colors, markers, font styles, and axes properties.
* **Multiple Formats:** Export figures to SVG, PDF, PNG, etc.

---

## 2. Matplotlib Get Started

To start using Matplotlib, install it along with NumPy (used for handling numerical arrays/data):

```bash
pip install matplotlib numpy
```

### Verification Script
Run the following script to check if the installation succeeded:
```python
import matplotlib
print("Matplotlib version:", matplotlib.__version__)
```

---

## 3. Matplotlib Pyplot

Most of the Matplotlib utilities lie under the `pyplot` submodule, and are usually imported under the `plt` alias:

```python
import matplotlib.pyplot as plt
```

Now, the `plt` object can be used to draw all kinds of plots.

---

## 4. Matplotlib Plotting

The `plot()` function is used to draw points (markers) or lines in a diagram. By default, it draws a line from point to point. It takes parameters for specifying points in the diagram:
* **Parameter 1:** An array containing the points on the **x-axis**.
* **Parameter 2:** An array containing the points on the **y-axis**.

### 1. Plotting X and Y Points
To draw a line between specified coordinate points, pass two arrays representing the x-coordinates and y-coordinates:
```python
import matplotlib.pyplot as plt
import numpy as np

# Draw a line from (1, 3) to (8, 10)
x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points)
plt.show()
```

### 2. Plotting Without Line
To plot only the markers without drawing a connecting line, you can pass a third parameter such as `'o'` (which stands for rings/circles):
```python
import matplotlib.pyplot as plt
import numpy as np

# Draw two points at (1, 3) and (8, 10) without a line
x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points, 'o')
plt.show()
```

### 3. Multiple Points
You can plot as many points as you like. Just make sure you have the same number of points in both axes:
```python
import matplotlib.pyplot as plt
import numpy as np

# Draw a line through points (1, 3) -> (2, 8) -> (6, 1) -> (8, 10)
x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

plt.plot(x_points, y_points)
plt.show()
```

### 4. Default X-Points
If we do not specify the points on the x-axis, the x-axis points will automatically get the default values `[0, 1, 2, 3, ...]` (depending on the length of the y-points):
```python
import matplotlib.pyplot as plt
import numpy as np

# Plotting y-points only; x-points default to [0, 1, 2, 3, 4, 5]
y_points = np.array([2, 4, 5, 6, 7, 10])

plt.plot(y_points, 'o')  # Plot as points only
plt.show()
```

Refer to [`Basic.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Basic.py) for practical plotting examples.

---

## 5. Matplotlib Markers

You can use the keyword argument `marker` to emphasize each coordinate point with a specific symbol/marker.

* Implementation Reference: [`Basic.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Basic.py)

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Mark each point with a circle
plt.plot(y_points, marker='o')
plt.show()
```

### Marker Reference Table
You can choose any of these marker symbols:
| Marker Syntax | Description |
| :--- | :--- |
| `'o'` | Circle |
| `'*'` | Star |
| `'.'` | Point |
| `','` | Pixel |
| `'x'` | X |
| `'X'` | X (filled) |
| `'+'` | Plus |
| `'P'` | Plus (filled) |
| `'s'` | Square |
| `'d'` | Diamond |
| `'D'` | Diamond (filled) |
| `'p'` | Pentagon |
| `'H'` | Hexagon |
| `'v'` | Triangle Down |
| `'^'` | Triangle Up |
| `'<'` | Triangle Left |
| `'>'` | Triangle Right |

---

### Format Strings `fmt`
You can also use the shortcut string notation parameter `fmt` to specify the marker, line style, and color.
The format parameter is written with this syntax: `marker|line|color`

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# 'o:r' means Circle marker, Dotted line, Red color
plt.plot(y_points, 'o:r')
plt.show()
```

#### Line Reference
| Line Syntax | Description |
| :--- | :--- |
| `'-'` | Solid line |
| `':'` | Dotted line |
| `'--'` | Dashed line |
| `'-.'` | Dashed/dotted line |

#### Color Reference
| Color Syntax | Description |
| :--- | :--- |
| `'r'` | Red |
| `'g'` | Green |
| `'b'` | Blue |
| `'c'` | Cyan |
| `'m'` | Magenta |
| `'y'` | Yellow |
| `'k'` | Black |
| `'w'` | White |

---

### Marker Size
You can use the keyword argument `markersize` or the shorter version `ms` to set the size of the markers:

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Set the size of the markers to 20
plt.plot(y_points, marker='o', ms=20)
plt.show()
```

---

### Marker Color
You can use the keyword arguments `markeredgecolor` (or `mec`) and `markerfacecolor` (or `mfc`) to customize the colors of the markers:
* **`mec` (Marker Edge Color):** Set the color of the outline/edge of the marker.
* **`mfc` (Marker Face Color):** Set the color of the inside/face of the marker.

#### Use both `mec` and `mfc`
```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Set the marker edge to red (mec='r') and the marker face to green (mfc='g')
plt.plot(y_points, marker='o', ms=20, mec='r', mfc='g')
plt.show()
```

---

## 6. Matplotlib Line

You can customize the styling, color, width, and quantity of lines plotted on a figure.

* Implementation Reference: [`Linestyle.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Linestyle.py)

### 1. Linestyle
You can use the keyword argument `linestyle` to change the style of the plotted line:
```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

plt.plot(y_points, linestyle='dotted')
plt.show()
```

### 2. Shorter Syntax
The `linestyle` parameter can be written in a shorter syntax as `ls`:
```python
plt.plot(y_points, ls=':')
```

### 3. Line Styles Reference Table
You can choose any of these line styles:
| Style Name | Short Syntax | Description |
| :--- | :--- | :--- |
| `'solid'` (default) | `'-'` | Draws a solid line |
| `'dotted'` | `':'` | Draws a dotted line |
| `'dashed'` | `'--'` | Draws a dashed line |
| `'dashdot'` | `'-.'` | Draws a dashed-dotted line |
| `'None'` | `''` or `' '` | Draws no line (useful if you only want markers) |

---

### 4. Line Color
You can use the keyword argument `color` or the shorter `c` to set the color of the line:
* You can use standard names (like `'red'`, `'green'`, `'blue'`, `'black'`, etc.)
* You can use short color notations (like `'r'`, `'g'`, `'b'`, `'k'`, etc.)
* You can use hexadecimal color values (like `'#4CAF50'`, `'#FF5733'`, etc.)

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Set the line color to green using standard names, or hex values:
plt.plot(y_points, color='green')
# plt.plot(y_points, c='#4CAF50')
plt.show()
```

---

### 5. Line Width
You can use the keyword argument `linewidth` or the shorter `lw` to change the width of the line. The value is a floating-point number representing point width:

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Plot with a 20.5pt wide line:
plt.plot(y_points, lw=20.5)
plt.show()
```

---

### 6. Multiple Lines
You can plot multiple lines by using multiple `plt.plot()` functions, or by passing multiple x and y coordinate pairs within a single `plt.plot()` function.

#### Option A: Using multiple `plt.plot()` calls
```python
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()
```

#### Option B: Specifying multiple coordinate pairs in a single `plt.plot()`
The x and y values must come in pairs:
```python
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# Plotting both lines in one function call:
plt.plot(x1, y1, x2, y2)
plt.show()
```

## 7. Matplotlib Labels and Title

With Matplotlib, you can label the axes and add a title to your plot to make the visualization easy to understand.

* Implementation Reference: [`label&title.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/label&title.py)

### 1. Create Labels for a Plot
You can use the `xlabel()` and `ylabel()` functions to set a label for the x-axis and y-axis:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')
plt.show()
```

### 2. Create a Title for a Plot
You can use the `title()` function to set a title for the plot:
```python
plt.plot(x, y)
plt.title('Sports Watch Data')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')
plt.show()
```

### 3. Set Font Properties for Title and Labels
You can use the `fontdict` parameter in `xlabel()`, `ylabel()`, and `title()` to set font properties (like family, color, and size):
```python
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.plot(x, y)
plt.title('Sports Watch Data', fontdict=font1)
plt.xlabel('Average Pulse', fontdict=font2)
plt.ylabel('Calorie Burnage', fontdict=font2)
plt.show()
```

### 4. Position the Title
You can use the `loc` parameter in `title()` to position the title. Legal values are: `'left'`, `'right'`, and `'center'` (default):
```python
plt.plot(x, y)
plt.title('Sports Watch Data', loc='left')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')
plt.show()
```

---

## 8. Matplotlib Adding Grid Lines

You can display grid lines on your plot to make reading data coordinates easier.

* Implementation Reference: [`grid_line.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/grid_line.py)

### 1. Add Grid Lines to a Plot
You can use the `grid()` function to add grid lines to the plot:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid()
plt.show()
```

### 2. Specify Which Grid Lines to Display
You can use the `axis` parameter in the `grid()` function to specify which grid lines to display. Legal values are `'x'`, `'y'`, and `'both'` (default):
```python
# Display only grid lines for the x-axis:
plt.grid(axis='x')

# Display only grid lines for the y-axis:
# plt.grid(axis='y')
```

### 3. Set Line Properties for the Grid
You can set the line properties of the grid, like color, linestyle, and linewidth, by passing corresponding arguments to the `grid()` function:
```python
plt.grid(color='orange', linestyle='--', linewidth=0.5)
```

---

## 9. Matplotlib Subplot

With subplots, you can display multiple plots in a single figure.

* Implementation Reference: [`subplot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/subplot.py)

### 1. Display Multiple Plots
You can use the `subplot()` function to draw multiple plots side-by-side or on top of each other:
```python
import matplotlib.pyplot as plt
import numpy as np

# Plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()
```

### 2. The `subplot()` Function
The `subplot()` function takes three arguments that describe the layout of the figure. The layout is organized in rows and columns, represented by the first and second arguments. The third argument represents the index of the current plot:
* `plt.subplot(1, 2, 1)`: The figure has **1 row, 2 columns**, and this plot is the **first** plot.
* `plt.subplot(1, 2, 2)`: The figure has **1 row, 2 columns**, and this plot is the **second** plot.

#### Stacking Plots Vertically (2 rows, 1 column)
```python
# Plot 1:
plt.subplot(2, 1, 1)
plt.plot(x, y)

# Plot 2:
plt.subplot(2, 1, 2)
plt.plot(x, y)
```

#### Drawing 6 Plots (2 rows, 3 columns)
```python
plt.subplot(2, 3, 1)
plt.plot(x, y)

plt.subplot(2, 3, 2)
# ... repeat for indices 3, 4, 5, 6
```

### 3. Title
You can add a title to each individual subplot using the `title()` function:
```python
# Plot 1:
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# Plot 2:
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")
```

### 4. Super Title
You can add a title for the entire figure using the `suptitle()` function:
```python
# Plot 1:
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# Plot 2:
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")

# Set figure-level title:
plt.suptitle("MY SHOP")
plt.show()
```

---

## 10. Matplotlib Scatter

A scatter plot is used to display the relationship between two variables, where each observation is represented as a point on the grid.

* Implementation Reference: [`scatter_plot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/scatter_plot.py)

### 1. Creating Scatter Plots
Use the `scatter()` function to draw a scatter plot. It requires two arrays of the same length, one for the x-axis and one for the y-axis:
```python
import matplotlib.pyplot as plt
import numpy as np

# Age and speed of 13 cars
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)
plt.show()
```

### 2. Compare Plots
You can draw multiple scatter plots on the same figure to compare data (e.g., comparing speed observations from Day 1 and Day 2):
```python
# Day 1 data:
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x1, y1)

# Day 2 data:
x2 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x2, y2)

plt.show()
```

### 3. Colors
You can set your own custom color for all the markers using the `color` or `c` parameter:
```python
# Plot markers with a custom color name or Hex color:
plt.scatter(x1, y1, color='hotpink')
plt.scatter(x2, y2, color='#88c999')
```

### 4. Color Each Dot
If you want to assign a unique color to each dot, you can pass an array of colors to the `c` argument (note: you must use `c` for this, not `color`):
```python
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)
```

---

### 5. ColorMap
A colormap is a pre-defined list of colors, where each color has a value ranging from 0 to 100. Matplotlib has dozens of built-in colormaps.

### 6. How to Use the ColorMap
You can specify a colormap by passing the `cmap` parameter (e.g. `cmap='viridis'`) along with an array of values for the `c` parameter. To display the scale bar next to the chart, call `plt.colorbar()`:
```python
# Map numbers to colors on the 'viridis' colormap
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()
```

### 7. Available ColorMaps
Here are some commonly used built-in colormaps:
* `'viridis'` (Default)
* `'plasma'`
* `'inferno'`
* `'magma'`
* `'cividis'`
* `'rainbow'`
* `'Accent'`
* `'nipy_spectral'`

---

### 8. Size
You can change the size of each marker by passing an array of sizes to the `s` argument:
```python
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
plt.scatter(x, y, s=sizes)
```

### 9. Alpha
You can adjust the transparency of the markers using the `alpha` parameter (accepts values between `0.0` (fully transparent) and `1.0` (fully opaque)):
```python
plt.scatter(x, y, s=sizes, alpha=0.5)
```

### 10. Combine Color Size and Alpha
You can combine custom colors (via colormaps), sizes, and transparency values all in one single scatter plot:
```python
# Generate 100 random values
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()
```

---

## 11. Matplotlib Bars

With Matplotlib, you can display categories using vertical or horizontal bar charts.

* Implementation Reference: [`bar_plot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/bar_plot.py)

### 1. Creating Bars
You can use the `bar()` function to draw vertical bar charts:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()
```

### 2. Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the `barh()` function:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
```

### 3. Bar Color
You can use the `color` argument to set the color of the bars:
```python
# Set vertical/horizontal bars color:
plt.bar(x, y, color="red")
# plt.barh(x, y, color="#4CAF50")
```

### 4. Bar Width
You can use the `width` argument to set the width of vertical bars (the default width is `0.8`):
```python
# Draw 4 very thin vertical bars:
plt.bar(x, y, width=0.1)
plt.show()
```

### 5. Bar Height
For horizontal bars, use the `height` argument to adjust the bar thickness (the default height is `0.8`):
```python
# Draw 4 very thin horizontal bars:
plt.barh(x, y, height=0.1)
plt.show()
```

---

## 12. Matplotlib Histograms

### 1. Histogram
A histogram is a graph showing frequency distributions. It shows the number of observations within each given interval.

**Example:** Say you ask for the height of 250 people. You might end up with a histogram showing distribution values like this:
* 2 people from 140 to 145cm
* 5 people from 145 to 150cm
* 15 people from 151 to 156cm
* 31 people from 157 to 162cm
* 46 people from 163 to 168cm
* 53 people from 168 to 173cm
* 45 people from 173 to 178cm
* 28 people from 179 to 184cm
* 21 people from 185 to 190cm
* 4 people from 190 to 195cm

---

### 2. Create Histogram
In Matplotlib, we use the `hist()` function to create histograms. The `hist()` function reads an array of numbers and groups them into intervals (bins) to generate the chart.

For this example, we use NumPy to randomly generate an array of 250 values concentated around 170 (average height) with a standard deviation of 10.

* Implementation Reference: [`Histograms_plot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Histograms_plot.py)

#### A Normal Data Distribution by NumPy:
```python
import numpy as np

# Generate 250 values around mean 170, std dev 10
x = np.random.normal(170, 10, 250)
print(x)
```

**Output format (randomly generated array):**
```text
[167.62255766 175.32495609 152.84661337 165.50264047 163.17457988 162.29867872 ...]
```

#### Creating the Histogram:
Pass the generated array directly to `plt.hist()`:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
```

---

## 13. Matplotlib Pie Charts

With Pyplot, you can use the `pie()` function to draw pie charts.

* Implementation Reference: [`pie_chart.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/pie_chart.py)

### 1. Creating Pie Charts
The `pie()` function draws one wedge for each value in the array:
```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
```
By default, the plotting of the first wedge starts from the x-axis and moves counterclockwise. The size of each wedge is determined by dividing the value by the sum of all values: `x/sum(x)`.

---

### 2. Labels
Add labels to the pie chart with the `labels` parameter. It must be an array with one label for each wedge:
```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.show()
```

---

### 3. Start Angle
By default, the start angle is 0 degrees (at the x-axis). You can change it using the `startangle` parameter:
```python
# Start the first wedge at 90 degrees:
plt.pie(y, labels=mylabels, startangle=90)
plt.show()
```

---

### 4. Explode
To make one of the wedges stand out, use the `explode` parameter. It must be an array of values representing how far from the center each wedge is displayed:
```python
# Pull the "Apples" wedge 0.2 from the center of the pie:
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()
```

---

### 5. Shadow
Add a shadow to the pie chart by setting the `shadow` parameter to `True`:
```python
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()
```

---

### 6. Colors
Set the color of each wedge using the `colors` parameter:
```python
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()
```
You can use standard color names, hex color values, or short colors codes (`'r'`, `'g'`, `'b'`, `'c'`, `'m'`, `'y'`, `'k'`, `'w'`).

---

### 7. Legend
To add a list of explanations for each wedge, call the `legend()` function:
```python
plt.pie(y, labels=mylabels)
plt.legend()
plt.show()
```

---

### 8. Legend With Header
To add a header to the legend, pass the `title` parameter to the `legend()` function:
```python
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.show()
```
