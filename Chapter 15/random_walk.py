#! python3

print("Task 15.3 and 15.4 and 15.5")

from random import choice


class RandomWalk:
    """Class intended to generate a random walk."""

    def __init__(self, num_points=5000):
        """Initialization of wandering attributes."""
        self.num_points = num_points

        # The starting point has coordinates (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all points for a random walk."""

        # Performing steps until the expected number of points is achieved.
        while len(self.x_values) < self.num_points:

            # Determining the direction and distance to be traveled in this direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6])
            y_step = y_direction * y_distance

            # Rejection of movements that lead nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Determining the next values X i Y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
