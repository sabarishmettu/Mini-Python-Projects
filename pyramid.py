import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#coordinates of the four corners of the base of the pyramid
x = [1, 1, -1, -1]
y = [1, -1, -1, 1]
z = [0, 0, 0, 0]

#coordinates of the apex of the pyramid
apex = [0, 0, 1]

#Plotting the base of the pyramid
ax.plot_trisurf(x, y, z)

#Plotting the lines connecting the apex to the base
for i in range(len(x)):
    ax.plot([apex[0], x[i]], [apex[1], y[i]], [apex[2], z[i]])

plt.show()
