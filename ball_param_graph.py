# graph a ball parameter
from csv import reader
import matplotlib.pyplot as plt 
import numpy as np 
from drill_file_defines import *

drill_num = "973"

with open("DRL"+drill_num+".csv", 'r') as f:
    csv_reader = reader(f)
    for row in csv_reader:
      # print(row[0]) 
      if len(row[0]) == 0:
         ball_indexes = row
      if DELAY_DF[:-2] in row[0]:
         delay_values = row
      if LEVEL_DF[:-2] in row[0]:
         level_values = row
      if SCORE_METHOD_DF[:-2] in row[0]:
         score_method_values = row


# ball_index_arr = np.array(list(map(int,ball_indexes[1:])))
ball_index_arr = np.array(ball_indexes[1:])
level_arr = np.array(list(map(float,level_values[1:])))
delay_arr = np.array(list(map(float,delay_values[1:])))
score_method_arr = np.array(list(map(int,score_method_values[1:])))

#instantiate muliple plots with row N, column 1:
figure, axis = plt.subplots(3, 1) 

axis[0].plot(ball_index_arr, delay_arr) 
axis[0].set_title(DELAY_DF) 

axis[1].plot(ball_index_arr, level_arr) 
axis[1].set_title(LEVEL_DF) 

axis[2].plot(ball_index_arr, score_method_arr) 
axis[2].set_title(SCORE_METHOD_DF) 

plt.subplots_adjust(left=0.1,    # left has to be less than right
                    right=0.9,  
                    bottom=0.1,  # bottom has to be less than top
                    top=0.9,  
                    wspace=0.4,  # adjust if there are multiple columns
                    hspace=0.6)  # adjust for multiple rows
# plt.subplot_tool() 
plt.show() 
