#include <bits/stdc++.h>
using namespace std;
#define Point pair<int,int>
struct Phash {
    size_t operator()(Point const& p) const noexcept {
        return hash<size_t>{}((((size_t)p.first)<<32)+p.second);
    }
};
unordered_set<Point,Phash> seen;
char grid[101][101];
int m,n;
const vector<Point> ADJ = { {-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}, {0,-1}, {-1,-1} };
char at(Point p) {
    if (p.first >= m || p.first < 0 || p.second < 0 || p.second >= n) return 0;
    return grid[p.first][p.second];
}
pair<Point,Point> adj(Point p) {
    vector<Point> ret;
    for (auto &move: ADJ) {
        Point oth = {move.first+p.first, move.second+p.second};
        if (at(oth) == '#') ret.push_back(oth);
    }
    if (ret.size() != 2) exit(1);
    return {ret[0], ret[1]};
}
void loop(Point start) {
    seen.insert(start);
    pair<Point,Point> cur = adj(start);
    while (!seen.count(cur.first) && !seen.count(cur.second)) {
        seen.insert(cur.first), seen.insert(cur.second);
        pair<Point,Point> prev = cur;
        
        pair<Point,Point> tmp = adj(prev.first);
        if (seen.count(tmp.first)) cur.first = tmp.second;
        else cur.first = tmp.first;
        
        tmp = adj(prev.second);
        if (seen.count(tmp.first)) cur.second = tmp.second;
        else cur.second = tmp.first;
    }
    seen.insert(cur.first), seen.insert(cur.second);
}
int main() {
    scanf("%d %d\n", &m, &n);
    for (int y = 0; y < m; y++, grid[y][n] = !getchar())
        for (int x = 0; x < n; x++)
            grid[y][x] = getchar();

    int loops = 0;
    for (int y = 0; y < m; y++)
        for (int x = 0; x < n; x++) {
            if (seen.count({y,x})) continue;
            if (at({y,x}) != '#') continue;
            // we found a new amoeba
            loop({y,x});
            loops++;
        }
    printf("%d\n", loops);
}
