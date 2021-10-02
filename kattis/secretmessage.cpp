#include <bits/stdc++.h>
using namespace std;
int main() {
    int N; scanf("%d\n", &N);
    for (int i = 0; i < N; i++,putchar(10)) {
        string s; getline(cin, s);
        int L = ceil(sqrt(s.length()));
        char grid[L][L]; memset(grid, '*', L*L);
        int x = L-1, y = 0;
        for (int j = 0; j < s.length();) {
            grid[x][y++] = s[j++];
            if (y == L) y = 0, x--;
        }
        for (y = 0; y < L; y++) 
            for (x = 0; x < L; x++)
                if (grid[x][y] != '*') putchar(grid[x][y]);
    }
}
