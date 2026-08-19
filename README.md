# Matplotlib Practice & Reference Guide

Welcome to the **Matplotlib Study and Reference Repository**! This project contains a collection of Python scripts demonstrating the core concepts of [Matplotlib](https://matplotlib.org/)—from basic line plotting and mathematical equation visualization to complex multi-axes figures and structured layouts.

> [!NOTE]
> This repository serves as a self-paced guide for learning Matplotlib, complete with runnable code examples, parameter references, and conceptual explanations.

---

## Table of Contents

1. [What is Matplotlib?](#what-is-matplotlib)
2. [Installation](#installation)
3. [Quick Start & Import](#quick-start--import)
4. [Project Overview & Scripts](#project-overview--scripts)
5. [Visualizing Equations](#visualizing-equations)
    - [Linear Equations](#linear-equations)
    - [Quadratic Equations](#quadratic-equations)
6. [Understanding Figures & Axes](#understanding-figures--axes)
    - [Figure vs Axes](#figure-vs-axes)
    - [Arranging Multiple Custom Axes](#arranging-multiple-custom-axes)
7. [Creating Structured Layouts with Subplots](#creating-structured-layouts-with-subplots)
8. [Formatting & Styling Reference](#formatting--styling-reference)

---

## What is Matplotlib?

**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in data science, machine learning, and scientific research for plotting data.

Key features include:
* **Easy plotting:** Create plots, histograms, power spectra, bar charts, error charts, scatterplots, etc., with just a few lines of code.
* **Customizable:** Full control over line styles, font properties, axes properties, and more.
* **Exporting:** Export figures to various file formats (PNG, PDF, SVG, etc.) and interactive environments.

---

## Installation

You can install Matplotlib using package managers like `pip` or `conda`.

### Option 1: Using pip (Recommended)
Run the following command in your terminal:
```bash
pip install matplotlib numpy
```

### Option 2: Using Conda
If you are using the Anaconda distribution, run:
```bash
conda install matplotlib numpy
```

---

## Quick Start & Import

To use Matplotlib in your Python scripts or Jupyter Notebooks, you typically import the `pyplot` module. It is a standard convention to alias it as `plt`:

```python
import matplotlib.pyplot as plt

# Verify installation by printing the version
import matplotlib
print("Matplotlib version:", matplotlib.__version__)
```

### Simple Line Plot Example
Here is a quick example to plot a simple line:
```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, marker='o')

# Add titles and labels
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()
```

---

## Project Overview & Scripts

Here is a summary of the reference scripts available in this repository:

| Script File | Description | Key Matplotlib Features |
| :--- | :--- | :--- |
| [`Basic.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Basic.py) | Customizing markers, colors, line styles, and marker edges. | `plt.plot()`, `marker`, `ms`, `mec` |
| [`Liner_Equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Liner_Equation.py) | Plotting a linear equation (`y = mx + c`) using NumPy arrays. | `np.linspace()`, `plt.xlim()`, `plt.ylim()`, `plt.grid()`, `plt.savefig()` |
| [`quadratic_equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/quadratic_equation.py) | Plotting a quadratic curve (`y = ax^2 + bx + c`). | Mathematical expressions, plotting curves |
| [`matplotlib_figure_object.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_figure_object.py) | Creating figure containers and adding custom axes explicitly. | `plt.figure()`, `fig.add_axes()`, `ax.plot()`, `ax.set_title()` |
| [`matplotlib_mutiple_figures.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_mutiple_figures.py) | Positioning 6 different axes on a single figure canvas. | `fig.add_axes([left, bottom, width, height])` positioning |
| [`matplotlib_subplot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_subplot.py) | Creating structured grids of subplots. | `plt.subplots()`, sharing axes, `plt.tight_layout()` |

---

## Visualizing Equations

Using NumPy along with Matplotlib allows you to plot continuous mathematical functions easily.

### Linear Equations
A linear equation has the form `y = mx + c`, where `m` is the slope and `c` is the y-intercept. 
* Implementation: [`Liner_Equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Liner_Equation.py)

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate 400 points from -10 to 10
x = np.linspace(-10, 10, 400)
m, c = 2, 3
y = m * x + c

plt.plot(x, y, label='y = 2x + 3')
plt.title('Plot of the Linear Equation')
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.savefig('Linear-Equation.png')  # Save figure first!
plt.show()
```

### Quadratic Equations
A quadratic equation typically has the form `y = ax^2 + bx + c`.
* Implementation: [`quadratic_equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/quadratic_equation.py)

```python
import numpy as np
import matplotlib.pyplot as plt

a, b, c = 1, -4, 4
x = np.linspace(-1, 7, 400)
y = a * (x ** 2) + b * x + c

plt.plot(x, y, label='y = x^2 - 4x + 4')
plt.title('Plot of the Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
```

---

## Understanding Figures & Axes

### Figure vs Axes
* **Figure** (`fig`): The overall canvas window that holds all plots, titles, legends, etc.
* **Axes** (`ax`): The actual individual plot grid containing the x/y data, labels, and ticks.

* Implementation: [`matplotlib_figure_object.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_figure_object.py)

```python
# 1. Create a Figure container
fig = plt.figure(figsize=(8, 6))

# 2. Add an Axes container explicitly: [left, bottom, width, height] relative to figure (0 to 1)
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])

# 3. Plot and customize using Axes methods
ax.plot(x, y, label='Data')
ax.set_title('Custom Axes Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
```

### Arranging Multiple Custom Axes
You can position multiple Axes containers on the same figure canvas at custom fractional coordinates.
* Implementation: [`matplotlib_mutiple_figures.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_mutiple_figures.py)

```python
# Add multiple axes at manual positions:
axes_center = fig.add_axes([0.3, 0.3, 0.4, 0.4])
axes_top = fig.add_axes([0.3, 0.75, 0.4, 0.2])
axes_right = fig.add_axes([0.75, 0.3, 0.2, 0.4])
```

---

## Creating Structured Layouts with Subplots

Instead of specifying manual coordinates, you can use `plt.subplots(rows, cols)` to generate a grid of subplots automatically.
* Implementation: [`matplotlib_subplot.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/matplotlib_subplot.py)

```python
import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots with shared Y axes
fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharey=True)

# Plot onto individual subplots by index
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[1, 0].plot([1, 2, 3], [3, 2, 1])
axs[1, 1].plot([1, 2, 3], [9, 4, 1])

plt.tight_layout()  # Optimizes spacing between subplots
plt.show()
```

---

## Formatting & Styling Reference

For a quick reference of line formatting features, see [`Basic.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/Basic.py).

### Line Styles
* `'-'` : Solid line
* `':'` : Dotted line
* `'--'` : Dashed line
* `'-.'` : Dashed/dotted line

### Common Colors
* `'r'` : Red
* `'g'` : Green
* `'b'` : Blue
* `'c'` : Cyan
* `'m'` : Magenta
* `'y'` : Yellow
* `'k'` : Black
* `'w'` : White

### Marker Parameters
* `marker` : Marker style (e.g., `'o'`, `'*'`, `'.'`, `','`, `'x'`, `'+'`)
* `ms` : Marker Size
* `mec` : Marker Edge Color
* `mfc` : Marker Face Color


