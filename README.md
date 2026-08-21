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

The `subplots()` function is used to create layouts with multiple plots on a single figure container.

* Implementation Reference: [`subplot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/subplot.py)

```python
import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot on individual axes
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[1, 0].plot([1, 2, 3], [3, 2, 1])
axs[1, 1].plot([1, 2, 3], [9, 4, 1])

plt.tight_layout()  # Automatically adjusts subplot margins to avoid overlapping
plt.show()
```

---

## 10. Matplotlib Scatter

Use the `scatter()` function to draw a scatter plot. It requires two arrays of the same length, one for the x-axis and one for the y-axis.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)
x = np.random.normal(5.0, 1.0, 100)
y = np.random.normal(10.0, 2.0, 100)

plt.scatter(x, y, color='purple', alpha=0.7)
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

---

## 11. Matplotlib Bars

Use the `bar()` function to draw vertical bar charts, or `barh()` for horizontal bar charts.

```python
import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["A", "B", "C", "D"])
values = np.array([3, 8, 1, 10])

plt.bar(categories, values, color='#4CAF50', width=0.6)
plt.title("Bar Chart Example")
plt.show()
```

---

## 12. Matplotlib Histograms

Use the `hist()` function to create histograms. It takes an array of data and automatically groups them into intervals (bins).

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate random normal distribution data
data = np.random.normal(170, 10, 250)

plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram Example")
plt.show()
```

---

## 13. Matplotlib Pie Charts

Use the `pie()` function to draw pie charts. By default, the plotting starts from the x-axis and goes counter-clockwise.

```python
import matplotlib.pyplot as plt
import numpy as np

sizes = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.show()
```