# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HAIdkL4KT9rGVR_IKpK3eWYrI8qLdz3
"""



input = open("/content/input4.txt", 'r')
output = open("/content/output4.txt", 'w')



def makeset(u):
    master[u] = u
    sz[u] = 1

def find(u):
    if master[u] == u:
        return u
    master[u] = find(master[u])
    return master[u]

def unite(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    if sz[u] < sz[v]:
        master[u] = v
        sz[v] += sz[u]
    else:
        master[v] = u
        sz[u] += sz[v]
    return True

#=========================================
nmax = int(1e5) + 10
master = [0] * nmax
sz = [0] * nmax
edge_vertices = [] * nmax

node, edge = map(int, input.readline().split())
for i in range(1, node+1):
    makeset(i)

edges = [] # [(cost, index)] pair

for i in range(edge):
    u, v, c = input.readline().split(' ')
    u = int(u)
    v = int(v)
    c = int(c)
    edge_vertices.append((u, v))
    edges.append((c, i))

edges.sort()


mst_cost = 0
edge_cnt = 0

for E in edges:
    u = edge_vertices[E[1]][0]
    v = edge_vertices[E[1]][1]

    if find(u) == find(v):
        continue

    unite(u, v)
    mst_cost += E[0]
    edge_cnt += 1
    #print(f"Taking {u} - {v} with cost {E[0]}")

if edge_cnt == node-1:
    print(mst_cost, file = output)
else:
    print("No mst", file = output)



input.close()
output.close()