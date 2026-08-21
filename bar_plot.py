# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np 

#Draw 4 bars:
x = np.array(['A' , 'B', 'C' , 'D'])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()


#Draw 4 horizontal bars:
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.barh(x,y)
plt.show()


#Draw 4 red bars:
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

plt.barh(x,y, color = 'red')
plt.show()


#Draw 4 very thin bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y , width = 0.1)
plt.show()


#Note: For horizontal bars, use height instead of width.
#Draw 4 very thin bars:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x,y, height = 0.1)
plt.show()


