#include <bits/stdc++.h>
using namespace std;
bool vis[1001];
vector<int> toposort;
unordered_set<int> seeing;
void dfs(unordered_set<int> *adjls, int v) {
    if (vis[v]) return;
    if (seeing.count(v)) exit(!puts("0"));
    seeing.insert(v);
    for (auto &oth: adjls[v]) dfs(adjls, oth);
    vis[v] = true;
    toposort.push_back(v);
    seeing.erase(v);
}
int main() {
    int k,n; scanf("%d %d\n", &k, &n);
    unordered_set<int> adjls[k+1];
    for (int i = 0; i < n; i++) {
        int p[3];
        char c;
        scanf("%d%c%d%*c%d", p, &c, p+1, p+2);
        for (auto &[fr,to]: vector<pair<int,int>>{c == '>' ? make_pair(0,1) : make_pair(1,2), make_pair(0,2)})
            adjls[p[fr]].insert(p[to]);
    }
    for (int i = 1; i < k+1; i++)
        if (!vis[i]) dfs(adjls,i);
    for (auto it = toposort.rbegin(); it != toposort.rend(); it++) printf("%d ", *it);
}
