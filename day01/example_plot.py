import matplotlib.pyplot as plt

def plot(x1, y1, x2, y2, x3, y3, **kwargs):
    filename = 'xy_chart.png'
    if 'filename' in kwargs:
        filename = kwargs['filename']
    # Sample data
    #x = [1, 2, 3, 4, 5]
    #y = [2, 3, 5, 7, 11]

    # Create the plot
    plt.plot(x1, y1, marker='o', linestyle='-', color='b')
    plt.plot(x2, y2, marker='o', linestyle='-', color='r')
    plt.plot(x3, y3, linestyle='-', color='g')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple XY Chart')
    plt.grid(True)

    # Save the plot to a PNG file
    plt.savefig(filename)

    # Optional: close the plot to free memory
    plt.close()
