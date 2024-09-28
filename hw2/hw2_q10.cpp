#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;

    vector<pair<int, int>> problems(t);
    for (int i = 0; i < t; ++i) {
        int a, b;
        cin >> a >> b;
        problems[i] = make_pair(a, b);
    }

    // Set the maximum number
    int max_num = 5000000;

    // Sieve of Eratosthenes to mark prime numbers
    vector<bool> is_prime(max_num + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= max_num; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= max_num; j += i) {
                is_prime[j] = false;
            }
        }
    }

    // Get all prime numbers up to max_num
    vector<int> prime_numbers;
    for (int i = 2; i <= max_num; ++i) {
        if (is_prime[i]) {
            prime_numbers.push_back(i);
        }
    }

    // Count number of prime factors
    vector<int> num_prime_factors(max_num + 1, 0);
    for (int a = 2; a <= max_num; ++a) {
        if (is_prime[a]) {
            num_prime_factors[a] = 1;
            continue;
        }

        for (int prime : prime_numbers) {
            if (a % prime == 0) {
                num_prime_factors[a] = 1 + num_prime_factors[a / prime];
                break;
            }
        }
    }

    // Sum of all prime factors up to max_num
    vector<long long> sum_of_prime_factors(max_num + 1, 0);
    for (int a = 2; a <= max_num; ++a) {
        sum_of_prime_factors[a] = sum_of_prime_factors[a - 1] + num_prime_factors[a];
    }

    // Answer the queries
    for (const auto &p : problems) {
        int a = p.first;
        int b = p.second;
        cout << sum_of_prime_factors[a] - sum_of_prime_factors[b] << endl;
    }

    return 0;
}
