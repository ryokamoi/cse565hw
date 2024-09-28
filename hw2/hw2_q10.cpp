#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int MAX_NUM = 5000000;

// Function to count prime factors of a number
int count_prime_factors(int num, const vector<int>& prime_numbers, const vector<bool>& is_prime, vector<int>& num_prime_factors) {
    if (num <= 1) return 0;
    if (is_prime[num]) return 1;

    for (int prime : prime_numbers) {
        if (num % prime == 0) {
            return 1 + num_prime_factors[num / prime];
        }
    }
    return 0;
}

int main() {
    int t;
    cin >> t;

    vector<pair<int, int>> problems(t);
    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        problems[i] = make_pair(a, b);
    }

    // Get all prime numbers up to MAX_NUM
    vector<bool> is_prime(MAX_NUM + 1, true);
    is_prime[0] = false;
    is_prime[1] = false;

    for (int i = 2; i <= sqrt(MAX_NUM); i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAX_NUM; j += i) {
                is_prime[j] = false;
            }
        }
    }

    vector<int> prime_numbers;
    for (int i = 2; i <= MAX_NUM; i++) {
        if (is_prime[i]) {
            prime_numbers.push_back(i);
        }
    }

    // Sum of all prime factors up to MAX_NUM
    vector<int> num_prime_factors(MAX_NUM + 1, 0);
    vector<int> sum_of_prime_factors(MAX_NUM + 1, 0);

    for (int a = 2; a <= MAX_NUM; a++) {
        num_prime_factors[a] = count_prime_factors(a, prime_numbers, is_prime, num_prime_factors);
        sum_of_prime_factors[a] = sum_of_prime_factors[a - 1] + num_prime_factors[a];
    }

    // Output the results for each problem
    for (const auto& problem : problems) {
        int a = problem.first;
        int b = problem.second;
        cout << sum_of_prime_factors[a] - sum_of_prime_factors[b] << endl;
    }

    return 0;
}
