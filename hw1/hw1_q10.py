n, m = [int(x) for x in input().split()]

a_list = [int(x) for x in input().split()]
b_list = [int(x) for x in input().split()]

roads_list = []
for _ in range(m):
    roads_list.append([int(x) for x in input().split()])


if sum(a_list) != sum(b_list):
    print("NO")
    exit()
    

# construct a flow network
graph: list[list[int]] = [[0 for _ in range(2*n+2)] for _ in range(2*n + 2)]
for i in range(1, n+1):
    graph[0][i] = a_list[i-1]
    graph[n+i][2*n+1] = b_list[i-1]
    
    graph[i][n+i] = 1000000000  # remain in the same city

for v_from, v_to in roads_list:
    graph[v_from][n+v_to] = 1000000000
    graph[v_to][n+v_from] = 1000000000

flow: list[list[int]] = [[0 for _ in range(2*n+2)] for _ in range(2*n + 2)]


# Edmonds-Karp algorithm
def bfs(graph: list[list[int]], flow: list[list[int]], s: int, t: int) -> list[int]:
    parent = [-1 for _ in range(len(graph))]
    parent[s] = -2
    q = [s]
    while q:
        node = q.pop(0)
        for i in range(len(graph)):
            if parent[i] == -1 and graph[node][i] - flow[node][i] > 0:
                parent[i] = node
                q.append(i)
    return parent


def edmonds_karp(graph: list[list[int]], flow: list[list[int]], s: int, t: int) -> tuple[int, list[list[int]]]:
    max_flow = 0
    while True:
        parent = bfs(graph, flow, s, t)
        if parent[t] == -1:
            break
        path_flow = 1000000000
        s = t
        while s != 0:
            path_flow = min(path_flow, graph[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = t
        while v != 0:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
    return max_flow, flow


max_flow, flow = edmonds_karp(graph, flow, 0, 2*n+1)

# print(max_flow)
# for row in flow:
#     print(row)


if sum(a_list) == max_flow:
    print("YES")
    
    for i in range(1, n+1):
        for j in range(n+1, 2*n+1):
            print(flow[i][j], end=" ")
        print()
else:
    print("NO")
