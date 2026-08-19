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

You can use the keyword argument `marker` to emphasize each coordinate point with a specific marker.

* Implementation Reference: [`Basic.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Basic.py)

```python
import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([3, 8, 1, 10])

# Mark each point with a circle ('o'), set size (ms=20), and outline color (mec='r')
plt.plot(y_points, marker='o', ms=20, mec='r')
plt.show()
```

### Marker Reference Table
| Marker | Description |
| :--- | :--- |
| `'o'` | Circle |
| `'*'` | Star |
| `'.'` | Point |
| `'x'` | X |
| `'+'` | Plus |

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



