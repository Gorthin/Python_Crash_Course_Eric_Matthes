#! python3

print("Task 15.1 and 15.2")

import matplotlib.pyplot as plt

x_values = range(5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

#Define the chart title and axis labels
ax.set_title("Cubes of numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 20)
ax.set_ylabel("Cubes of value", fontsize = 20)

#Define size axis labels
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)
#Defining the scope for each axis
ax.axis([0, 5100, 0, 130_000_000_000])

plt.show()