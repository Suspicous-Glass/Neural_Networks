#A histogram is an approximate representation of the distribution of numerical data. 

#program sets up an array of sudorandom integers using a matrix of histograms
import numpy as np
import time as t

n = np.random.randint(0,10,10000) #10,000 matracies of [0,9]
hh = np.bincount(n) #counts amount of each number, 1-9.
h = np.bincount(n) #this is going to be used for percentage
h = h / h.sum() #prob of the combination 

print(hh)
print(h)

#histograms will eventually be used for image recognition, language models, and other neural nets of that type

