#include <stdio.h>
#define NMAX 1024000
int parent[NMAX];
int Rank[NMAX];
inline int findset(int a) {
    while (parent[a] != a) {
        a = parent[a] = parent[parent[a]];
    } // no idea what the nesting is for
    return a;
}
inline void swap(int *m, int *n) {
    int tmp = *m;
    *m = *n;
    *n = tmp;
}
int main() {
    int n,q; scanf("%d %d\n", &n, &q);
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < q; i++) {
        char op;
        int a, b;
        scanf("%c %d %d\n", &op, &a, &b);
        if (op == '=') {
            int x = findset(a), y = findset(b);
            if (x != y) {
                if (Rank[x] < Rank[y]) swap(&x,&y);
                parent[y] = x;
                Rank[x] += Rank[y];
            }
        } else puts(findset(a) == findset(b) ? "yes" : "no");
    }
}
