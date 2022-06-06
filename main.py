import random
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = comm.Get_size()

DATA = 0
average = 0

neighs = []
avgTempOfLayers = []
avgTempOfAllNodes = []

sumOfLayerTemp = 0
sumOfAllLayerTemp = 0

msg = [-1, -1, -1]  # message types
msg[0], msg[1], msg[2] = rank, DATA, "HELLO"

A = np.array([
    #  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],  # 9
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # 10
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],  # 12
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],  # 13
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],  # 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],  # 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],  # 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],  # 18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],  # 19
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]  # 20
])

# neighbors
msg[0], msg[1], msg[2] = rank, DATA, "HELLO"

for j in range(0, n):
    if A[rank, j] == 1:
        neighs.append(j)
print("rank upper: {}, neighs: {}".format(rank, neighs))

for node in neighs:
    tempData = random.randint(10, 30)
    comm.send(tempData, dest=node, tag=DATA)

for node in neighs:
    tempData = comm.recv(source=node, tag=DATA)
    avgTempOfLayers.append(tempData)
    print("rank: {}, neigh[{}] --> temp: {}, tempArray: {}".format(rank, node, tempData, avgTempOfLayers))
    sumOfLayerTemp += tempData
    average = sumOfLayerTemp / len(avgTempOfLayers)

avgTempOfAllNodes.append(average)
print("current average temperature of layer: {}".format(average))

n = len(avgTempOfAllNodes)  # taking the size of average temp of layers array
n = n - 1  # size - 1 = the latest index of array
print("avgTempOfAllNodes: {} size: {}".format(avgTempOfAllNodes[n], len(avgTempOfAllNodes)))

print("\n")
