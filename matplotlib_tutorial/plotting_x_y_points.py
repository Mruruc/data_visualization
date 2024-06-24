"""
The plot() function is used to draw points(markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.

first parameter is an array containing the points on the x-axis,
second parameter is an array containing the points on the y-axis.

"""
import matplotlib.pyplot as plt

# plt.plot([0, 1, 0.2, 5, 6, 7], [5, 10, 15, 10, 15, 50])
# plt.show()

# plt.plot([10, 20, 50, 30, 10, 100], marker='3')
# plt.show()


# plt.plot([10, 20, 50, 30, 10, 100], '*-.g', ms=10)
# plt.show()

plt.plot([10, 20, 50, 30, 10, 100], '*:g', ms=15, mfc='r')
plt.show()
