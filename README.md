# Python Matplotlib Reference Guide

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

You can use the keyword argument `linestyle` or `ls` to change the style of the plotted line.

* Implementation Reference: [`Linestyle.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Linestyle.py)

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Style the line as dashed ('--'), make it green, and set the line width (lw=2.5)
plt.plot(y_points, ls='--', color='green', lw=2.5)
plt.show()
```

### Line Formatting Options
* **Styles (`linestyle` / `ls`):**
  * `'solid'` or `'-'` (Default)
  * `'dotted'` or `':'`
  * `'dashed'` or `'--'`
  * `'dashdot'` or `'-.'`
* **Width (`linewidth` / `lw`):** Accepts a float representing point width (e.g., `lw=20.5`).

---

## 7. Matplotlib Labels

Use the `xlabel()` and `ylabel()` functions to add labels to the axes, and the `title()` function to add a title to the plot.

* Implementation Reference: [`label&title.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/label&title.py)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = 2 * x + 3

plt.plot(x, y)
plt.title("Linear Equation Plot")
plt.xlabel("X Axis Value")
plt.ylabel("Y Axis Value")
plt.show()
```

---

## 8. Matplotlib Grid

Use the `grid()` function to add gridlines to the plot. You can customize the axis (e.g., `axis='x'`), line style, color, and width of the grid.

* Implementation Reference: [`Liner_Equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Liner_Equation.py)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
```

---

## 9. Matplotlib Subplot

The `subplots()` function is used to create layouts with multiple plots on a single figure container.

* Implementation Reference: [`matplotlib_subplot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_subplot.py)

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
