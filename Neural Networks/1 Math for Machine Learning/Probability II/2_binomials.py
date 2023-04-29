#Math as seen on pgs. 46-47
#An alternative to histograms when attempting to create "discrete distrobution"
import numpy as np

t = np.random.binomial(5, .3, size=1000)
s = np.bincount(t)
print(s)
print(s / s.sum())
