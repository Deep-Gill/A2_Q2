import matplotlib.pyplot as plt
import pandas as pd

# x axis values
x = [1, 2, 3, 4, 5, 6]
# corresponding y axis values
y = [2, 4, 1, 5, 2, 6]

data = pd.read_csv("./rs_1.csv")

print(data)

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
          marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(0,1)
plt.xlim(1,100000)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Q2. (a)')

# function to show the plot
plt.show()