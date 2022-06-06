from mpi4py import MPI
import random as rand
import numpy as np
import math
import networkx as nx


def randfunc():
    number = rand.randint(10, 30)
    return number


class nodeClass:
    def __init__(self, data):
        self.data = data


root = nodeClass(data=0)
a = nodeClass(data=randfunc())
b = nodeClass(data=randfunc())
c = nodeClass(data=randfunc())
d = nodeClass(data=randfunc())
e = nodeClass(data=randfunc())
f = nodeClass(data=randfunc())
g = nodeClass(data=randfunc())
h = nodeClass(data=randfunc())
i = nodeClass(data=randfunc())
j = nodeClass(data=randfunc())
k = nodeClass(data=randfunc())
L = nodeClass(data=randfunc())
m = nodeClass(data=randfunc())
n = nodeClass(data=randfunc())
o = nodeClass(data=randfunc())
p = nodeClass(data=randfunc())
r = nodeClass(data=randfunc())
s = nodeClass(data=randfunc())
t = nodeClass(data=randfunc())
u = nodeClass(data=randfunc())

graph = {
    root: [a, b, c, d, e],
    a: [root, b, f, g],
    b: [root, c, g, f, h],
    c: [root, d, h, i, g],
    d: [root, e, i, h, j],
    e: [root, j, i],
    f: [a, b, g, k, L],
    g: [a, b, c, f, h, k, L, m],
    h: [b, c, d, g, i, L, m, n],
    i: [c, d, e, h, j, m, n, o],
    j: [d, e, i, n, o],
    k: [f, g, L, p, r],
    L: [f, g, h, k, m, p, r, s],
    m: [g, h, i, L, n, r, s, t],
    n: [h, i, j, m, o, s, t, u],
    o: [i, j, n, t, u],
    p: [k, L, r],
    r: [k, L, m, p, s],
    s: [L, m, n, r, t],
    t: [m, n, o, s, u],
    u: [n, o, t]
}
# initializations
d = 4
visited = []  # List for visited nodes.
queue = []  # Initialize a queue
