#include <bits/stdc++.h>
using namespace std;
#define Point pair<int,int>
struct Phash {
    size_t operator()(Point const& p) const noexcept {
        return hash<size_t>{}((((size_t)p.first)<<32)+p.second);
    }
};
int N;
int grid[101][101];
int main() {
    scanf("%d\n", &N);
    Point pos;
    for (int y = 1; y <= N; y++,getchar())
        for (int x = 1; x <= N; x++)
            if ((grid[x][y] = getchar()) == 'K') pos = {y,x};
    //
    queue<pair<Point,int>> border; border.push({pos,0});
    unordered_set<Point,Phash> seen;
    while (!border.empty()) {
        auto [cur,dist] = border.front(); border.pop();
        if (seen.count(cur)) continue;
        if (cur == make_pair(1,1)) return !printf("%d\n", dist);
        auto &[r,c] = cur;
        seen.insert(cur);
        for (auto &[y,x]: {make_pair(r+2,c+1), make_pair(r+2,c-1), make_pair(r-2,c+1), make_pair(r-2,c-1), make_pair(r+1,c+2), make_pair(r+1,c-2), make_pair(r-1,c+2), make_pair(r-1,c-2)}) {
            if (x < 1 || y < 1 || x > N || y > N || grid[x][y] == '#') continue;
            border.push({make_pair(y,x),dist+1});
        };
    }
    puts("-1");
}
