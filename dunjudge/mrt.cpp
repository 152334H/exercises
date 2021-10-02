#include <bits/stdc++.h>
#define INF 2000000001
using namespace std;
int main() {
    int n, e, Q;
    scanf("%d %d %d\n", &n, &e, &Q);
    long long adjm[n][n];
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++)
        adjm[i][j] = (i!=j)*INF;
    for (int i = 0; i < e; i++) {
        int x,y,t;
        scanf("%d %d %d\n", &x, &y, &t);
        adjm[x][y] = adjm[y][x] = t;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                adjm[j][k] = adjm[k][j] = min(adjm[k][j], adjm[k][i]+adjm[i][j]);
    for (int i = 0; i < Q; i++) {
        int a,b;
        scanf("%d %d\n", &a, &b);
        printf("%d\n", adjm[a][b] == INF ? -1 : adjm[a][b]);
    }
}
