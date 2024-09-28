n, m = map(int, input().split())

node_char = input()
node_char = " " + node_char  # 1-based index

graph: list[set] = [set() for _ in range(n+1)]
inverse_graph: list[set] = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    inverse_graph[v].add(u)

# if the graph is not DAG, the value can be arbitrary large
# topological sort to find cycle
sorted_vertices = []
node_added = [False for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visiting = [False for _ in range(n+1)]
for v in range(1, n+1):
    if not visited[v]:
        stack = [v]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                visiting[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                    elif visiting[neighbor]:
                        print(-1)
                        exit()
            else:
                visiting[node] = False
                stack.pop()
                
                if not node_added[node]:
                    sorted_vertices.append(node)
                    node_added[node] = True

sorted_vertices = sorted_vertices[::-1]

def char_to_int(c):
    return ord(c) - ord('a')

# DP over the topological order

# print(graph)
# print(sorted_vertices)
ans = 0
for c in range(26):
    dp = [0 for _ in range(n+1)]
    for v in sorted_vertices:
        for neighbor in inverse_graph[v]:
            dp[v] = max(dp[v], dp[neighbor])
 
        if c == char_to_int(node_char[v]):
            dp[v] += 1
    
    ans = max(ans, max(dp))

# for r in dp:
#     print(r)

print(ans)
