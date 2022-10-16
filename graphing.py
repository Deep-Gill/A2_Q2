import matplotlib.pyplot as plt
import pandas as pd



data = pd.read_csv("./rs_1.csv")

array = data.to_numpy()
y = []
rTrue = 0
rFalse = 0



def yFunction(rTrue, rFalse):
    total = rTrue + rFalse
    return rTrue / total


for value in array:
    if value[0] == 1:
        rTrue += 1
    if value[0] == 2:
        rFalse += 1
    y.append(yFunction(rTrue, rFalse))

x = []
for i in range(1, 100000):
    x.append(i)
    # print(i)


print(rTrue + rFalse)
# plotting the points
plt.plot(x, y, color='blue', linestyle='solid', linewidth = 1,
          marker=',', markerfacecolor='blue', markersize=2)

# setting x and y axis range
plt.ylim(0,0.5)
plt.xlim(1,100000)
plt.xscale('log')
# naming the x axis
plt.xlabel('Number of samples')
# naming the y axis
plt.ylabel('P(R = T | s+, w+)')

# giving a title to my graph
plt.title('Q2. (a)')

# function to show the plot
plt.show()