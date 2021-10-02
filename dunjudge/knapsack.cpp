#include <bits/stdc++.h>
using namespace std;
typedef struct {
    int v;
    int w;
} Item;
map<int,int> weight_index[2048]; //w_i[weight] -> some sorted dict of (value,count)
map<pair<int,int>,int> dp;
vector<Item> arr;
int dpat(int n, int w) {
    if (dp[{n,w}]) return dp[{n,w}];
    if (n == 0 || w <= 0) return dp[{n,w}] = 0;
    return dp[{n,w}] = max(max(dpat(n-1,w), dpat(n,w-1)), dpat(n-1,w-arr[n-1].w)+arr[n-1].v);
}
int main() {
    int S, N; scanf("%d %d\n", &S, &N);
    for (int i = 0; i < N; i++) {
        int v,w,k; scanf("%d %d %d\n", &v, &w, &k);
        weight_index[w][v] += k;
    }
    for (int w = 1; w <= 2000; w++) {
        auto &d = weight_index[w];
        int k_max = S/w;
        for (auto it = d.rbegin(); it != d.rend(); it++) {
            int k = min(it->second,k_max);
            k_max -= k;
            while (k--) arr.push_back({it->first,w});
        }
    }
    printf("%d\n", dpat(arr.size(), S));
}
