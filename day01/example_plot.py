import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple XY Chart')
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('xy_chart.png')

# Optional: close the plot to free memory
plt.close()