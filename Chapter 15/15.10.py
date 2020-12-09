from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=500):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# Visualizing with Pygal
from IPython.display import HTML, display, SVG
import pygal

while True:
    rw = RandomWalk()
    rw.fill_walk()
    xy_chart = pygal.XY()
    xy_chart.title = 'Random Walk'
    rwValues = list(zip(rw.x_values, rw.y_values))
    xy_chart.add('rw', rwValues)
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        display({'image/svg+xml': xy_chart.render()}, raw=True)
        # OR
        xy_chart.render_in_browser()
        # OR
        display(SVG(xy_chart.render(disable_xml_declaration=True)))
        break