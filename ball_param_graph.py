# graph a ball parameter
from csv import reader
import matplotlib.pyplot as plt 
import numpy as np 

with open('DRL001.csv', 'r') as f:
    csv_reader = reader(f)
    for row in csv_reader:
      if len(row[0]) == 0:
         ball_indexes = row
      if "DELAY" in row[0]:
         delay_values = row
x = np.array(list(map(int,ball_indexes[1:])))
y = np.array(list(map(float,delay_values[1:])))
  
plt.plot(x, y)  # Plot the chart 
plt.show() 

# print(ball_indexes[1:])
# print(delay_values[1:])

