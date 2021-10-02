#include <bits/stdc++.h>
using namespace std;
/*
struct LCA {
    vector<int> height, euler, first, segtree;
    vector<bool> visited;
    int n;

    LCA(vector<vector<int>> &adj, int root = 0) {
        n = adj.size();
        height.resize(n); first.resize(n);
        euler.reserve(n*2);
        visited.assign(n,false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m*4);
        build(1,0,m-1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to: adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h+1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) segtree[node] = euler[b];
        else {
            int mid = (b+e)/2;
            build(node<<1, b, mid);
            build(node<<1|1, mid+1, e);
            int l = segtree[node<<1], r = segtree[node<<1|1];
            segtree[node] = (height[l]<height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L) return -1;
        if (b >= L && e <= R) return segtree[node];
        int mid = (b+e) >> 1;
        int left = query(node << 1, b, mid, L, R);
        int right = query(node<<1|1, mid+1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right) swap(left,right);
        return query(1, 0, euler.size()-1, left, right);
    }
};
*/
int main() {
    int N; scanf("%d\n", &N);
    unordered_map<int,int> adjls[N+1];// {start: {end: weight}}
    //vector<vector<int>> adj; adj.resize(N+1); // another thing
    long long d[N+1]; //dist from 1 to node x
    for (int i = 0; i < N-1; i++) {
        int a,b,h; scanf("%d %d %d\n", &a, &b, &h);
        adjls[b][a] = -(adjls[a][b] = h);
        //adj[a].push_back(b); adj[b].push_back(a);
    }
    // generate LCA from node 1... suboptimal probably.
    //LCA lca(adj, 1);
    bool vis[N+1] = {0};
    stack<pair<int,long long>> S; // {node, distto}
    S.push({1,0});
    while (!S.empty()) {
        auto [cur,w] = S.top(); S.pop();
        if (vis[cur]) continue;
        vis[cur] = true;
        d[cur] = w;
        for (auto [oth,ow]: adjls[cur])
            S.push({oth,ow+w});
    }
    int Q; scanf("%d\n", &Q);
    for (int q = 0; q < Q; q++) {
        int x,y; scanf("%d %d\n", &x, &y);
        //printf("%d+%d-2*%d == ", d[x], d[y], d[lca.lca(x,y)]);
        //printf("%d\n", d[x]+d[y]-2*d[lca.lca(x,y)]);
        printf("%lld\n", d[y]-d[x]); // wtf?
    }
}
