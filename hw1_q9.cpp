#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>

using namespace std;


vector<int> color_list;
vector<int> ordered_vertices;

void explore(const unordered_map<int, vector<int>>& graph, int v, int color) {
    color_list[v] = color;
    
    for (int edge : graph.at(v)) {
        if (color_list[edge] == -1) {
            explore(graph, edge, color);
        }
    }

    ordered_vertices.insert(ordered_vertices.begin(), v);
}


void dfs(const unordered_map<int, vector<int>>& graph, const vector<int>& vertices) {
    int color = 1;
    for (int v : vertices) {
        if (color_list[v] == -1) {
            explore(graph, v, color);
            color++;
        }
    }
}


int main() {
    // Load inputs
    int num_junction;
    cin >> num_junction;

    vector<int> junctions_cost(num_junction);
    for (int i = 0; i < num_junction; ++i) {
        cin >> junctions_cost[i];
    }

    int road_num;
    cin >> road_num;
    vector<pair<int, int>> roads_list(road_num);

    for (int i = 0; i < road_num; ++i) {
        int e_from, e_to;
        cin >> e_from >> e_to;
        roads_list[i] = {e_from - 1, e_to - 1};
    }

    // Construct the graph (adjacency list)
    unordered_map<int, vector<int>> graph, inverse_graph;
    for (int jnc = 0; jnc < num_junction; ++jnc) {
        graph[jnc] = {};
        inverse_graph[jnc] = {};
    }

    for (int i = 0; i < road_num; ++i) {
        int e_from = roads_list[i].first;
        int e_to = roads_list[i].second;
        graph[e_from].push_back(e_to);
        inverse_graph[e_to].push_back(e_from);
    }

    // Initialize global variables
    color_list.assign(num_junction, -1);
    ordered_vertices.clear();

    // DFS on inverse graph
    vector<int> vertices(num_junction);
    for (int i = 0; i < num_junction; ++i) {
        vertices[i] = i;
    }
    dfs(inverse_graph, vertices);

    // copy ordered vertices
    vector<int> ordered_vertices_copy = ordered_vertices;

    // DFS on original graph with the ordered vertices from the inverse graph
    color_list.assign(num_junction, -1);
    dfs(graph, ordered_vertices_copy);

    // Calculate the price and number of combinations
    long long price = 0;
    long long combinations = 1;
    const int MOD = 1000000007;

    unordered_map<int, vector<int>> scc_cost_dict;
    for (int i = 0; i < num_junction; ++i) {
        scc_cost_dict[color_list[i]].push_back(junctions_cost[i]);
    }

    for (int scc = 1; scc <= *max_element(color_list.begin(), color_list.end()); ++scc) {
        int min_price = *min_element(scc_cost_dict[scc].begin(), scc_cost_dict[scc].end());
        price += min_price;

        int count_min_price = count(scc_cost_dict[scc].begin(), scc_cost_dict[scc].end(), min_price);
        combinations = (combinations * count_min_price) % MOD;
    }

    // Output result
    cout << price << " " << combinations << endl;
}
