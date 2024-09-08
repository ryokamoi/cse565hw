from typing import List

# load inputs
num_junction = int(input())
junctions_cost = [int(j) for j in input().split()]

road_num = int(input())
roads_list = []
for _ in range(road_num):
    v_from, v_to = [int(j) - 1 for j in input().split()]
    roads_list.append((v_from, v_to))

# construct a graph (adjacent list)
graph: dict[int, list[int]] = {}
inverse_graph: dict[int, list[int]] = {}
for jnc in range(num_junction):
    graph[jnc] = []
    inverse_graph[jnc] = []

for i in range(road_num):
    v_from, v_to = roads_list[i]
    graph[v_from].append(v_to)
    inverse_graph[v_to].append(v_from)


def explore(graph, v, color, ordered_vertices: list[int]):
    global color_list
    color_list[v] = color
    
    for to_v in graph[v]:
        if color_list[to_v] is None:
            ordered_vertices = explore(graph, to_v, color, ordered_vertices)
    
    ordered_vertices.append(v)
    return ordered_vertices


def dfs(graph: dict[int, list[int]], vertices: List[int]):
    ordered_vertices = []
    
    global color_list
    color: int = 1
    for v in vertices:
        if color_list[v] is None:
            ordered_vertices = explore(graph, v, color, ordered_vertices)
            color += 1
    
    return ordered_vertices[::-1]


# We need to make a police checkpoint in each SCC
# create inverse graph to get order of vertices
color_list = [None for _ in range(num_junction)]
order = dfs(inverse_graph, list(range(num_junction)))

# SCC algorithm
color_list = [None for _ in range(num_junction)]
_ = dfs(graph, order)

price = 0
combinations = 1

scc_cost_dict: dict[int, list] = {}
for color, cost in zip(color_list, junctions_cost):
    scc_cost_dict.setdefault(color, []).append(cost)

for scc in range(1, max(color_list)+1):
    min_price = min(scc_cost_dict[scc])
    price += min_price
    
    combinations *= scc_cost_dict[scc].count(min_price)
    combinations %= 1000000007

print(price, combinations)
