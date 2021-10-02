#include <bits/stdc++.h>
using namespace std;
#define Point(y,x) ((y<<16)+(short)x)
#define X(p) (p&0xffff)
#define Y(p) (p>>16)
int main() {
    int r,c; scanf("%d %d\n", &r, &c);
    char grid[r][c+2];
    for (int y = 0; y < r; y++)
        fgets(grid[y], c+2, stdin);
    //
    int pools = 0;
    for (int y = 0; y < r; y++)
        for (int x = 0; x < c; x++)
            if (grid[y][x] == 'H') { // check current tile && floodfill if needed
                queue<int> border; border.push(Point(y,x));
                unordered_set<int> seen;
                while(!border.empty()) {
                    int cur = border.front(); border.pop();
                    int cy = Y(cur), cx = X(cur);
                    if (cy < 0 || cx < 0 || cy >= r || cx >= c) continue;
                    if (seen.count(cur)) continue;
                    if (grid[cy][cx] != 'H') continue;
                    seen.insert(cur);
                    grid[cy][cx] = '.';
                    for (auto &v: {Point(-1,0), Point(1,0), Point(0,1), Point(0,-1)})
                        border.push(v+cur);
                }
                pools++;
            }
    printf("Oh, bother. There are %d pools of hunny.", pools);
}
