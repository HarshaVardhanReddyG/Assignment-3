import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

read = pd.read_excel("raw_table.xlsx","Sheet1")

# creating the dataset
data = np.array(read)
Political_party = data[0]
Seats_won = data[1]
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(Political_party,Seats_won, color ='maroon',
        width = 0.4)
 
plt.xlabel("Political party ")
plt.ylabel("No. of seats won")
plt.title("Seats won by different political parties")
plt.show()