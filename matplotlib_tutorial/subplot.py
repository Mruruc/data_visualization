import matplotlib.pyplot as plt

"""
subplot() function takes three arguments that describes the layout of the figure.
The layout is organized in rows and columns, which are represented by the first and second argument.
The third argument represents the index of the current plot.
example:
# plt.subplot(1, 2, 1)
# the figure has 1 row, 2 columns, and this plot is the first plot.
"""

# Sample weather data
months = ['January', 'February',
          'March', 'April', 'May',
          'June', 'July', 'August',
          'September', 'October', 'November', 'December'
          ]

avg_temp = [5.0, 6.0, 10.0, 15.0, 20.0, 25.0, 30.0, 29.0, 24.0, 18.0, 12.0, 7.0]
precipitation = [78, 60, 55, 42, 35, 25, 20, 22, 30, 45, 65, 80]

# suptitle() adds title to entire figure

plt.suptitle("2023 Temperature and Precipitation Statics")

# plot 1:
plt.subplot(2, 1, 1)
plt.plot(months, avg_temp, color='darkred', linestyle='-')
plt.title("2023 Monthly Average Temperature")
plt.xlabel("Months")
plt.ylabel("(°C)")
plt.xticks(rotation=45)
plt.grid()

# plot 2:
plt.subplot(2, 1, 2)
plt.plot(months, precipitation, '*:', color='#00ffff', markersize=10)

plt.title("2023 Monthly Average Precipitation")
plt.xlabel("Months")
plt.ylabel("Precipitation (mm)")
plt.xticks(rotation=45)
plt.grid()

# Adjust layout to prevent clipping of labels
plt.tight_layout()

plt.show()
