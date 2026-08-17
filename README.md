## What is Matplotlib?

**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in data science, machine learning, and scientific research for plotting data.

Key features include:
- **Easy plotting:** Create plots, histograms, power spectra, bar charts, error charts, scatterplots, etc., with just a few lines of code.
- **Customizable:** Full control over line styles, font properties, axes properties, and more.
- **Exporting:** Export figures to various file formats (PNG, PDF, SVG, etc.) and interactive environments.

---

## How to Install Matplotlib

You can install Matplotlib using package managers like `pip` or `conda`.

### Option 1: Using pip (Recommended)
Run the following command in your terminal or command prompt:

```bash
pip install matplotlib
```

### Option 2: Using Conda
If you are using the Anaconda distribution, run:

```bash
conda install matplotlib
```

---

## How to Import Matplotlib

To use Matplotlib in your Python scripts or Jupyter Notebooks, you typically import the `pyplot` module. It is a standard convention to alias it as `plt`:

```python
import matplotlib.pyplot as plt

# Verify installation by printing the version
import matplotlib
print("Matplotlib version:", matplotlib.__version__)
```

### Simple Usage Example

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

## Plotting Equations with NumPy and Matplotlib

You can also use NumPy along with Matplotlib to plot mathematical functions, such as linear and quadratic equations.

A script demonstrating how to plot a linear equation is available at [`readme/Liner_Equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/readme/Liner_Equation.py).

### Linear Equation Example (`y = 2x + 3`)

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate x values using NumPy
x = np.linspace(start=-10, stop=10, num=400)

# 2. Define the linear equation parameters (y = mx + c)
m = 2  # Slope
c = 3  # Y-intercept
y = m * x + c

# 3. Create the plot
plt.plot(x, y, label='y = 2x + 3')
plt.title('Plot of the Linear Equation')
# Limit axes to focus on specific ranges if desired
plt.xlim(0, 10)
plt.ylim(0, 20)

# 4. Add formatting and legend
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# 5. Save and show the plot
plt.savefig('Linear-Equation.png')  # Note: Save before show() to avoid blank images
plt.show()
```

### Quadratic Equation Example (`y = x^2 - 4x + 4`)

A quadratic equation typically has the form `y = ax^2 + bx + c`. A script demonstrating this is available at [`quadratic_equation.py`](file:///c:/Users/Ajith%20Kumar/Desktop/matplotlib/quadratic_equation.py).

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Define coefficients
a = 1
b = -4
c = 4

# 2. Generate x values
x = np.linspace(-1, 7, 400)

# 3. Calculate y values
y = a * (x ** 2) + b * x + c

# 4. Create the plot
plt.plot(x, y, label='y = x^2 - 4x + 4')
plt.title('Plot of the Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# 5. Display the plot
plt.show()
```

---
