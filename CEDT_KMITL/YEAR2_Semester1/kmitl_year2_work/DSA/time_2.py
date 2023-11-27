import numpy as np
from sklearn.neighbors import NearestNeighbors
import random
import time

r = lambda: random.randint(0,10000)

samples = [[r(),r(),r()] for i in range(1000000)]
testdat = [[r(),r(),r()] for i in range(1000)]
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(samples)

detect1 = neigh.kneighbors(testdat)

detect2=[]
for i in testdat:
    detect2 += neigh.kneighbors([i])