#include <bits/stdc++.h>
using namespace std;
#define SIZE 1000
/*
 * dp(y,x,sz) = dp(y,x,sz-1) && [summed array stuff]
 * dp(y,x,1) = material[y][x]
 */
#define bzero(arr) memset(arr, 0, sizeof arr);
#define area(x,y,sz) sat[y+sz][x+sz]+sat[y][x]-sat[y+sz][x]-sat[y][x+sz]
int findMaxSquare(int material[SIZE][SIZE], int materialSize) {
    int sat[SIZE+1][SIZE+1];
    bzero(sat);
    for (int y = 1; y <= materialSize; y++)
        for (int x = 1; x <= materialSize; x++)
            sat[y][x] = sat[y][x-1]+material[y-1][x-1];
    for (int y = 1; y <= materialSize; y++)
        for (int x = 1; x <= materialSize; x++)
            sat[y][x]+= sat[y-1][x];
    int maxsz = 0, count = 0;
    for (int y = 0; y < materialSize; y++)
        for (int x = 0; x < materialSize; x++) {
            if (!material[y][x]) {
                continue;
            }
            // this square has not be subsumed yet
            int sz = 0;
            while (++sz) {
                if (max(x+sz,y+sz) >= materialSize) break;
                if (area(x,y,sz+1) != (sz+1)*(sz+1)) break;
            }
            if (sz > maxsz) {
                maxsz = sz; count = 1;
            } else if (sz == maxsz) count++;
            //printf("(%d,%d): maxsz==%d count==%d\n", y,x,maxsz,count);
        }
    return count*maxsz;
}
int main() {
    int grid[SIZE][SIZE] = {{0,1,1,1,1,0}, {1,0,1,1,1,1}, {0,1,1,1,1,1}, {1,1,0,1,1,1}, {1,1,1,1,0,1}, {1,1,0,1,1,1}};
    printf("%d\n", findMaxSquare(grid, 6));
}
