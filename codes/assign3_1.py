import numpy as np
import matplotlib.pyplot as plt
# creating the dataset
data = {'A':75, 'B':55, 'C':37,
        'D':29, 'E':10, 'F':37 }
Political_party = list(data.keys())
Seats_won = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(Political_party,Seats_won, color ='maroon',
        width = 0.4)
 
plt.xlabel("Political party ")
plt.ylabel("No. of seats won")
plt.title("Seats won by different political parties")
plt.show()