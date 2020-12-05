#! python3
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Create a new random walk while the program remains active.
while True:
    # Prepare random walk data.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Display random walk points.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)

    # Highlight the first and last points of a random walk.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # Hide the axis.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another random walk? (y / n): ")
    if keep_running == 'n':
        break
