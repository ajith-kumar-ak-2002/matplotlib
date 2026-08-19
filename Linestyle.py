# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np  

# #Use a dotted line:
# y_point = np.array([3, 8 , 1 , 10])

# plt.plot(y_point , linestyle = 'dotted')
# plt.plot(y_point, linestyle = 'dashed')
# plt.show()

'''
Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.

Line Styles
You can choose any of these styles:

Style	            Or
'solid'         (default)	'-'	
'dotted'            ':'	
'dashed'            '--'	
'dashdot'           '-.'	
'None'	            '' or ' '

'''



# #Set the line color to red:
# y_point = np.array([3, 8, 1, 10])

# plt.plot(y_point , color = 'green')
# plt.show()


# #Plot with a 20.5pt wide line:
# y_point = np.array([3, 8, 1, 10])

# plt.plot(y_point, lw = 20.5)
# plt.show()



# #Draw two lines by specifying a plt.plot() function for each line:
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

'''
You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:

'''
# Example
# Draw two lines by specifiyng the x- and y-point values for both lines:


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
