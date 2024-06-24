import matplotlib.pyplot as plt

# sample weather data:

months = ['January', 'February',
          'March', 'April', 'May',
          'June', 'July', 'August',
          'September', 'October', 'November', 'December']

avg_temp = [5.0, 6.0, 10.0, 15.0, 20.0, 25.0, 30.0, 29.0, 24.0, 18.0, 12.0, 7.0]

# xlabel() and ylabel() functions to set a label for the x- and y-axis.
# title() function to set a title for the plot.
# fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.


# grid() function to add grid lines to the plot

plt.figure(figsize=(10, 5))

plt.plot(months, avg_temp, 'o:')

font1 = {
    'family': 'serif',
    'color': 'red',
    'size': 20
}
font2 = {
    'family': 'serif',
    'color': 'darkred',
    'size': 15
}

plt.title("2023 Monthly Average Temperature", font1)
plt.xlabel("Months", fontdict=font2)
plt.ylabel("Average Temperature", fontdict=font2)

# grid() function to add grid lines to the plot
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
