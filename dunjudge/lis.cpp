#include <bits/stdc++.h>
using namespace std;
int v[5120];
int lis[5120];
int main() {
    int N; scanf("%d\n", &N);
    int ma = 0;
    for (int i=0; i<N; i++) {
        scanf("%d", v+i);
        for (int j = 0; j < i; j++) 
            if (v[j] < v[i] && lis[j] > lis[i])
                lis[i] = lis[j];
        lis[i]++;
        if (lis[i] > ma) ma = lis[i];
    }
    printf("%d\n", ma);
}
