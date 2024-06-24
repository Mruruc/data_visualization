import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Furniture', 'Clothing', 'Groceries',
              'Toys', 'Sports Equipment']
january_sales = [15000, 8000, 10500, 18000, 7500, 5000]
february_sales = [14500, 8500, 11000, 17500, 8000, 5500]
march_sales = [16200, 9200, 11800, 19000, 8300, 6200]

# Setting the positions and width for the bars
bar_width = 0.25

# Create initial positions for the first set of bars
r1 = list(range(len(categories)))

# Shift positions for the second set of bars
r2 = [x + bar_width for x in r1]

# Shift positions for the third set of bars
r3 = [x + bar_width for x in r2]

# Create the bar chart
plt.figure(figsize=(12, 8))

# Plotting the bars
plt.bar(r1, january_sales, color='b', width=bar_width, edgecolor='grey', label='January')
plt.bar(r2, february_sales, color='g', width=bar_width, edgecolor='grey', label='February')
plt.bar(r3, march_sales, color='r', width=bar_width, edgecolor='grey', label='March')

# Adding labels
plt.xlabel('Product Category', fontweight='bold')
plt.ylabel('Sales ($)', fontweight='bold')
plt.title('Quarterly Sales by Product Category')
plt.xticks([r + bar_width for r in range(len(categories))], categories, rotation=30)
plt.legend()

# Show the plot
plt.show()
