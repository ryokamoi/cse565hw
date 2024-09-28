#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

int n, m;
string node_char;
vector<set<int>> graph;
vector<set<int>> inverse_graph;
vector<int> sorted_vertices;
vector<bool> node_added;
vector<bool> visited;
vector<bool> visiting;

void topological_sort(int v) {
    stack<int> s;
    s.push(v);
    while (!s.empty()) {
        int node = s.top();
        if (!visited[node]) {
            visited[node] = true;
            visiting[node] = true;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    s.push(neighbor);
                } else if (visiting[neighbor]) {
                    cout << -1 << endl;
                    exit(0); // Cycle detected
                }
            }
        } else {
            visiting[node] = false;
            s.pop();
            if (!node_added[node]) {
                sorted_vertices.push_back(node);
                node_added[node] = true;
            }
        }
    }
}

int char_to_int(char c) {
    return c - 'a';
}

int main() {
    // Input n and m
    cin >> n >> m;

    // Input node characters and prepend a space (for 1-based indexing)
    cin >> node_char;
    node_char = " " + node_char;

    // Initialize graph and inverse_graph as vector of sets
    graph.resize(n + 1);
    inverse_graph.resize(n + 1);
    
    // Input edges
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].insert(v);
        inverse_graph[v].insert(u);
    }

    // Initialize topological sorting helpers
    node_added.resize(n + 1, false);
    visited.resize(n + 1, false);
    visiting.resize(n + 1, false);

    // Perform topological sort
    for (int v = 1; v <= n; ++v) {
        if (!visited[v]) {
            topological_sort(v);
        }
    }

    // Reverse the sorted vertices for correct topological order
    reverse(sorted_vertices.begin(), sorted_vertices.end());

    // DP over the topological order
    int ans = 0;
    for (int c = 0; c < 26; ++c) {
        vector<int> dp(n + 1, 0);
        for (int v : sorted_vertices) {
            for (int neighbor : inverse_graph[v]) {
                dp[v] = max(dp[v], dp[neighbor]);
            }
            if (c == char_to_int(node_char[v])) {
                dp[v]++;
            }
        }
        ans = max(ans, *max_element(dp.begin(), dp.end()));
    }

    // Output the answer
    cout << ans << endl;

    return 0;
}
