#include <bits/stdc++.h>
using namespace std;
#define Pos pair<long long,int>
int main() {
    int V, E, C, K, M; scanf("%d %d %d %d %d\n", &V, &E, &C, &K, &M);
    if (K > C && M > C) return !puts("-1");
    unordered_map<int,int> clearings[V+1]; // [clearing_no][other_clearing_no] == distance
    unordered_set<int> fruits;
    // get bulk input
    for (int i = 0; i < E; i++) {
        int u,v,w; scanf("%d %d %d\n", &u, &v, &w);
        clearings[u][v] = clearings[v][u] = w;
    }
    for (int i = 0, tmp; i < C; fruits.insert(tmp),i++) scanf("%d", &tmp);
    // idea: greedy solution of just grabbing the K nearest fruits via BFS
    priority_queue<Pos, vector<Pos>, greater<Pos>> border; border.push({0,1}); // start at 1, distance is 0.
    unordered_set<int> seen;
    while (!border.empty()) {
        auto [dist,v] = border.top(); border.pop();
        if (seen.count(v)) continue;
        seen.insert(v);
        if (fruits.count(v)) K--, M--;
        if (!K || !M) return !printf("%lld\n", dist*2);
        for (auto &[u,w]: clearings[v])
            border.push({dist+w,u});
    }
    puts("-1");
}
