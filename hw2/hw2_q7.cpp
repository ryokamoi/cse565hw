#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    // Input array
    vector<int> a(n + 1);  // 1-indexed
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    // c[j]: the number of sequences where length is i, i-th value is a_k where k <= j
    vector<int> c(n + 1, 0);
    vector<int> c_prev(n + 1, 0);

    // initialization
    for (int j = 1; j <= n; j++) {
        c_prev[j] = c_prev[j - 1] + 1;
    }

    // DP
    int ans = c_prev[n];
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[j] % i != 0) {
                c[j] = c[j - 1];
            } else {
                c[j] = c[j - 1] + c_prev[j - 1];
            }
        }

        ans += c[n];
        for (int j = 1; j <= n; j++) {
            c_prev[j] = c[j];
        }
    }

    cout << ans << endl;
    return 0;
}
