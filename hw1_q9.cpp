#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <climits>

using namespace std;

vector<long long> color_list;
vector<long long> ordered_vertices;

void explore(const unordered_map<long long, vector<long long>>& graph, long long v, long long color) {
    color_list[v] = color;
    
    for (long long edge : graph.at(v)) {
        if (color_list[edge] == -1) {
            explore(graph, edge, color);
        }
    }

    ordered_vertices.push_back(v);
}

void dfs(const unordered_map<long long, vector<long long>>& graph, const vector<long long>& vertices) {
    long long color = 1;
    for (long long v : vertices) {
        if (color_list[v] == -1) {
            explore(graph, v, color);
            color++;
        }
    }
}


int main() {
    // Load inputs
    long long num_junction;
    cin >> num_junction;

    vector<long long> junctions_cost(num_junction);
    for (long long i = 0; i < num_junction; ++i) {
        cin >> junctions_cost[i];
    }

    long long road_num;
    cin >> road_num;
    vector<pair<long long, long long>> roads_list(road_num);

    for (long long i = 0; i < road_num; ++i) {
        long long e_from, e_to;
        cin >> e_from >> e_to;
        roads_list[i] = {e_from - 1, e_to - 1};
    }

    // Construct the graph (adjacency list)
    unordered_map<long long, vector<long long>> graph, inverse_graph;
    for (long long jnc = 0; jnc < num_junction; ++jnc) {
        graph[jnc] = {};
        inverse_graph[jnc] = {};
    }

    for (long long i = 0; i < road_num; ++i) {
        long long e_from = roads_list[i].first;
        long long e_to = roads_list[i].second;
        graph[e_from].push_back(e_to);
        inverse_graph[e_to].push_back(e_from);
    }

    // Initialize global variables
    color_list.assign(num_junction, -1);
    ordered_vertices.clear();

    // DFS on inverse graph
    vector<long long> vertices(num_junction);
    for (long long i = 0; i < num_junction; ++i) {
        vertices[i] = i;
    }
    dfs(inverse_graph, vertices);

    // Reverse the ordered vertices
    reverse(ordered_vertices.begin(), ordered_vertices.end());

    // DFS on original graph with the ordered vertices from the inverse graph
    color_list.assign(num_junction, -1);
    dfs(graph, ordered_vertices);

    // Calculate the price and number of combinations
    long long price = 0;
    long long combinations = 1;
    const long long MOD = 1000000007;

    unordered_map<long long, pair<long long, long long>> scc_min_cost; // Stores {min_cost, count}

    for (long long i = 0; i < num_junction; ++i) {
        long long color = color_list[i];
        long long cost = junctions_cost[i];
        
        if (scc_min_cost.find(color) == scc_min_cost.end()) {
            scc_min_cost[color] = {cost, 1};
        } else {
            if (cost < scc_min_cost[color].first) {
                scc_min_cost[color] = {cost, 1};
            } else if (cost == scc_min_cost[color].first) {
                scc_min_cost[color].second++;
            }
        }
    }

    for (const auto& [color, min_cost_count] : scc_min_cost) {
        price += min_cost_count.first;
        combinations = (combinations * min_cost_count.second) % MOD;
    }

    // Output result
    cout << price << " " << combinations << endl;
}
