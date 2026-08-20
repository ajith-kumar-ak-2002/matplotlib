# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np

#Draw a line in a diagram from position (0,0) to position (6,250):
x_point = np.array([0,6])
y_point = np.array([0,250])

plt.plot(x_point, y_point)
plt.show()


#Draw a line in a diagram from position (1, 3) to position (8, 10):
x_point = np.array([1,3])
y_point = np.array([8,10])

plt.plot(x_point, y_point)
plt.show()


#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
x_point = np.array([1,3])
y_point = np.array([8,10])

plt.plot(x_point , y_point, 'o')
plt.show()


#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
x_point = np.array([1,2,6,8])
y_point = np.array([3,8,1,10])

plt.plot(x_point, y_point)
plt.show()


#Plotting without x-points:
y_point = np.array([2,4,5,6,7,10])

plt.plot(y_point, 'o')
plt.show()


#Mark each point with a circle:
x_point = np.array([2,5,7,8])
y_point = np.array([4,5,7,10])

plt.plot(x_point, y_point, marker = 'o')
plt.plot(x_point, y_point, marker = '*')
plt.show()


#Mark each point with a circle:
y_point = np.array([3, 8, 1 , 10])

plt.plot(y_point, 'o:r')
plt.show()

'''
Line Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line


Color Reference
Color Syntax	Description
        'r'	Red	
        'g'	Green	
        'b'	Blue	
        'c'	Cyan	
        'm'	Magenta	
        'y'	Yellow	
        'k'	Black	
        'w'	White


'''


#Set the size of the markers to 20:
y_point = np.array([3, 8, 1, 10])

plt.plot(y_point , marker = 'o', ms = 20)
plt.show()


#Set the EDGE color to red:
y_point = np.array([3, 8, 1, 10])

plt.plot(y_point , marker = 'o', ms = 20 , mec = 'r')