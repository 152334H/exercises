#include <bits/stdc++.h>
using namespace std;
int main() {
    int N; scanf("%d\n", &N);
    unordered_map<int,int> goodstofrom[N+1];
    unordered_map<int,int> goodsfromto[N+1];
    int required[N+1];
    for (int n = 1; n <= N; n++) {
        int K; scanf("%d %d", required+n, &K);
        for (int k = 0, s,v; k < K; k++) {
            scanf("%d %d", &s, &v);
            goodsfromto[s][n] = goodstofrom[n][s] = v;
        }
    }
    unordered_set<int> dead; dead.insert(1);
    queue<int> collapsing;
    for (auto &[to,v]: goodsfromto[1]) collapsing.push(to);
    while (!collapsing.empty()) {
        int cur = collapsing.front(); collapsing.pop();
        if (dead.count(cur)) continue;
        int goods = 0; // might be worth caching this but...
        for (auto &[fr,v]: goodstofrom[cur])
            if (!dead.count(fr)) goods += v;
        if (goods >= required[cur]) continue; // did not collapse
        dead.insert(cur);
        for (auto &[to,v]: goodsfromto[cur]) collapsing.push(to);
    }
    printf("%d\n", N-dead.size());
}
