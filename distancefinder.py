matrix = []


Q = []
distance = []
pre_node = []
for i in range(len(matrix):
    Q.append(i)
    distance.append(100)
    pre_node.append(-1)
    Q.append(i)

distance[0] = [0]

while len(Q) != 0:
    u = Q[0]
    Q.pop(0)
    for v in Q
        if matrix[u][v] > 0:
            a=distance[u] + matrix[u][v]
            if a < distance[v]:
               distance[v]=a
               pre_node[v] = u
print(distance)
    
