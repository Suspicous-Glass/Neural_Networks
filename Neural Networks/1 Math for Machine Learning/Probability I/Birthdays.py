import numpy as np

for m in range(2,31):
    matches = 0
    for n in range(100000):
        match = 0
        b = np.random.randint(0,364,m)
        for i in range(m):
            for j in range(m):
                if (i != j) and (b[i] == b[j]):
                    match += 1
        if (match != 0):
            matches +=1

    print("%2d %0.6f" % (m, matches/100000))
