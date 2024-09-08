from typing import List

# load inputs
num_junction = int(input())
junctions_cost = [int(j) for j in input().split()]

road_num = int(input())
roads_list = []
for _ in range(road_num):
    e_from, e_to = [int(j) - 1 for j in input().split()]
    roads_list.append((e_from, e_to))

# construct a graph (adjacent list)
graph: dict[int, list[int]] = {}
for jnc in range(num_junction):
    graph[jnc] = []

for i in range(road_num):
    e_from, e_to = roads_list[i]
    graph[e_from].append(e_to)


def explore(graph, v, color):
    color_list[v] = color
    
    for edge in graph[v]:
        if color_list[edge] is None:
            explore(graph, edge, color)
    
    global ordered_vertices
    ordered_vertices = [v] + ordered_vertices


def dfs(graph: dict[int, list[int]], vertices: List[int]):
    global color_list
    color: int = 1
    for v in vertices:
        if color_list[v] is None:
            explore(graph, v, color)
            color += 1


# We need to make a police checkpoint in each SCC
# create inverse graph to get order of vertices
inverse_graph: dict[int, list[int]] = {}
for v in range(num_junction):
    inverse_graph[v] = []

for v, edges in graph.items():
    for to_v in edges:
        inverse_graph[to_v].append(v)

color_list = [None for _ in range(num_junction)]
ordered_vertices = []
dfs(inverse_graph, list(range(num_junction)))

# SCC algorithm
color_list = [None for _ in range(num_junction)]
dfs(graph, ordered_vertices)

price = 0
combinations = 1

scc_cost_dict: dict[str, list] = {}
for color, cost in zip(color_list, junctions_cost):
    scc_cost_dict.setdefault(color, []).append(cost)

for scc in range(1, max(color_list)+1):
    min_price = min(scc_cost_dict[scc])
    price += min_price
    
    combinations *= scc_cost_dict[scc].count(min_price)
    combinations %= 1000000007

print(price, combinations)
