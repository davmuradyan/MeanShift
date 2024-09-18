import numpy as np
import Plot

data = np.array([[2, 7], [3, 5], [3, 6], [3, 8], [4, 4], [4, 5], [4, 6], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [6, 5], [6, 7]])
data = np.array([np.array(point) for point in data])


def Distance(a, b):
    a = np.array(a)
    b = np.array(b)
    d = np.sqrt(np.sum((a - b) ** 2))
    d = float(d)
    return d
def FindClosePoints(point, data, radius):
    point = np.array(point)
    close_points = []

    for p in data:
        if np.sqrt(np.sum((p - point)**2)) <= radius:
            close_points.append(p)
    return close_points

def FindNewMean(close_points):
    if len(close_points) == 1:
        return close_points[0]

    mean = [(close_points[0][0] + close_points[1][0]) / 2, (close_points[0][1] + close_points[1][1]) / 2]
    for i in range(2, len(close_points)):
        mean = [(mean[0] + close_points[i][0]) / 2, (mean[1] + close_points[i][1]) / 2]
    return list(map(float, mean))

def GetCentroids(means, eps):
    means = means.tolist()
    centroids = [means[0]]

    for i in range(1, len(means)):
        distances = []
        for centroid in centroids:
            distances.append(Distance(means[i], centroid))
        close = False

        for d in distances:
            if d <= eps:
                close = True

        if not close:
            centroids.append(means[i])
    return centroids


def MeanShift(data, radius, eps = 0.0001):
    close_points = []
    previous_means = data
    new_means = []

    while True:
        for point in previous_means:
            close_points = FindClosePoints(point, previous_means, radius)
            mean = FindNewMean(close_points)
            new_means.append(mean)
        new_means = np.array(new_means)
        previous_means = np.array(previous_means)

        if np.linalg.norm(new_means - previous_means) < eps:
            break
        previous_means = new_means
        previous_means = list(previous_means)
        new_means = []

    centroids = GetCentroids(previous_means, eps)
    clusters = [[] for _ in centroids]
    Plot.plot_data(centroids)
    Plot.plot_data(data)

    for point in data:
        minDistance = np.inf
        minIndex = np.inf
        for i in range(len(clusters)):
            distance = np.sqrt(np.sum((point - centroids[i])**2))
            if distance < minDistance:
                minDistance = distance
                minIndex = i
        clusters[minIndex].append(point)
    print(clusters)
    return clusters


MeanShift(data, 1)