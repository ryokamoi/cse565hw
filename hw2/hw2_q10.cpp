#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {
    int t;
    // cin >> t;
    scanf("%d", &t);

    vector<pair<int, int>> problems;
    for (int i = 0; i < t; i++) {
        int a, b;
        // cin >> a >> b;
        scanf("%d %d", &a, &b);
        problems.push_back({a, b});
    }

    // get all prime numbers up to max_num
    int max_num = 5000000;
    vector<bool> is_prime(max_num + 1, true);
    vector<int> prime_factor(max_num + 1, 0);
    is_prime[0] = false;
    is_prime[1] = false;
    
    for (int i = 2; i <= sqrt(max_num); i++) {
        if (is_prime[i]) {
            prime_factor[i] = i;
            for (int j = i * i; j <= max_num; j += i) {
                is_prime[j] = false;
                prime_factor[j] = i;
            }
        }
    }

    // get all prime numbers up to max_num
    vector<int> prime_numbers;
    for (int i = 0; i <= max_num; i++) {
        if (is_prime[i]) {
            prime_numbers.push_back(i);
        }
    }

    // count num of prime factors
    vector<int> num_prime_factors(max_num + 1, 0);
    for (int a = 2; a <= max_num; a++) {
        if (is_prime[a]) {
            num_prime_factors[a] = 1;
            continue;
        }
        num_prime_factors[a] = 1 + num_prime_factors[a / prime_factor[a]];
    }

    // sum of all prime factors up to max_num
    vector<int> sum_of_prime_factors(max_num + 1, 0);
    for (int a = 2; a <= max_num; a++) {
        sum_of_prime_factors[a] = sum_of_prime_factors[a - 1] + num_prime_factors[a];
    }

    // process each problem
    for (const auto& problem : problems) {
        int a = problem.first;
        int b = problem.second;
        // cout << sum_of_prime_factors[a] - sum_of_prime_factors[b] << endl;
        printf("%d\n", sum_of_prime_factors[a] - sum_of_prime_factors[b]);
    }

    return 0;
}
