# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np

# A simple pie chart:
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

# Pie chart with labels:
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels)
plt.show()

# Pie chart with custom start angle:
plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# Pie chart with explode:
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()

# Pie chart with shadow:
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()

# Pie chart with custom colors:
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()

# Pie chart with legend:
plt.pie(y, labels=mylabels)
plt.legend()
plt.show()

# Pie chart with legend and header:
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.show()
