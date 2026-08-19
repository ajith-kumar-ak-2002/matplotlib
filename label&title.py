# pyrefly: ignore [missing-import]
import _frozen_importlib_external
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
import numpy as np


# #Add labels to the x- and y-axis:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


# plt.plot(x,y)

# plt.xlabel('Average Pulse')
# plt.ylabel('Calorie Burnage')

# plt.show()


# #Add a plot title and labels for the x- and y-axis:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x,y)
# plt.title('Sports Watch Data')
# plt.xlabel('Average Pulse')
# plt.ylabel('Calorie Burnage')

# plt.show()



# #Set font properties for the title and labels:
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif', 'color':'red', 'size' : 20}
# font2 = {'family':'serif', 'color':'green', 'size':15}

# plt.plot(x,y)
# plt.title('Sports Watch Data', fontdict = font1)
# plt.xlabel('Average Pulse', fontdict = font2)
# plt.ylabel('Calorie Burnage', fontdict = font1)

# plt.show()



#Position the title to the left:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title("Sports Watch Data", loc = 'right')

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

