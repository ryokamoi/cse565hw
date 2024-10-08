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


def explore(graph, v, color, ordered_vertices: list[int], color_list: list[int]):
    added_set: set = set()
    stack = [v]
    while stack:
        node = stack[-1]
        if color_list[node] is None:
            color_list[node] = color
            all_visited = True
            
            for to_v in graph[node]:
                if color_list[to_v] is None:
                    stack.append(to_v)
                    all_visited = False
            if all_visited:
                ordered_vertices.append(stack.pop())
                added_set.add(node)
        else:
            stack.pop()
            if node not in added_set:
                ordered_vertices.append(node)
                added_set.add(node)
    
    return ordered_vertices, color_list


def dfs(graph: dict[int, list[int]], vertices: List[int], color_list: list[int]):
    ordered_vertices = []
    color = 1
    for v in vertices:
        if color_list[v] is None:
            ordered_vertices, color_list = explore(graph, v, color, ordered_vertices, color_list)
            color += 1
    
    return ordered_vertices[::-1], color_list


# We need to make a police checkpoint in each SCC
# create inverse graph to get order of vertices
color_list = [None for _ in range(num_junction)]
order, _ = dfs(inverse_graph, list(range(num_junction)), color_list)

# SCC algorithm
color_list = [None for _ in range(num_junction)]
_, color_list = dfs(graph, order, color_list)

# find the minimum cost for each SCC
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
