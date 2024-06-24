import matplotlib.pyplot as plt

# plt.plot([3, 8, 1, 10], linestyle='dotted')
# plt.plot([3, 8, 1, 10], linestyle='dashed')

# linestyle can be written as ls.
# dotted can be written as :.
# dashed can be written as --.

# plt.plot([3, 8, 1, 10], ls=':', color='g')

# we can use the keyword argument color or the shorter c to set the color of the line:
# plt.plot([3, 8, 1, 10], ls=':', color='g')
# plt.plot([3, 8, 1, 10], ls=':', c='#4CAF50')


# Line Width:
# linewidth or the shorter lw change the width of the line.

# plt.plot([5, 9, 11, 10], linewidth=3, marker='o', linestyle='dotted', color='r', markersize=10)
# plt.plot([5, 9, 11, 10], 'o:r', linewidth=3, markersize=10)

# Multiple Lines

# y1 = [1, 5, 9, 3, 1, 3]
# y2 = [5, 5, 9, 21, -6]
#
# plt.plot(y1, 'o:r', markersize=3)
# plt.plot(y2, '*-g', markersize=10)
# plt.show()
