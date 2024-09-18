import matplotlib.pyplot as plt

def plot_data(data):
    # Extract x and y coordinates
    x = [point[0] for point in data]
    y = [point[1] for point in data]

    # Plot the data points
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Data points')
    plt.title('Scatter Plot of Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()