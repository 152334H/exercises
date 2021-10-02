#include <bits/stdc++.h>
using namespace std;
int h,w; 
int dp[512][512];
int wall[512][512];
int gecko(int x, int y) {
    if (dp[y][x]) return dp[y][x];
    int ma = 0;
    for (int off = -1; off <= 1; off++)
        if (x+off >= 0 && x+off < w) ma = max(gecko(x+off,y+1),ma);
    return dp[y][x] = wall[y][x] + ma;
}
int main() {
    scanf("%d %d\n", &h, &w);
    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++) scanf("%d", &wall[i][j]);
    for (int x = 0; x < w; x++) dp[h-1][x] = wall[h-1][x];
    int ma = 0;
    for (int x = 0; x < w; x++) ma = max(ma, gecko(x,0));
    printf("%d\n", ma);
}
