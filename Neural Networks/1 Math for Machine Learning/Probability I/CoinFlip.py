import numpy as np 

N = 1000000 #iterations
M = 3 #coins 

heads = np.zeros(M+1)

for i in range(N):
    flips = np.random.randint(0,2,M)
    h, _ = np.bincount(flips, minlength=2)
    heads[h] += 1

prob = heads / N 
print("probabilities: %s" % np.array2string(prob)) #probability of 0,1,2, or 3 heads
