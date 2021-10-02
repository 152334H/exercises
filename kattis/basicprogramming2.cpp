#include <bits/stdc++.h>
using namespace std;
int main() {
    int N, t;
    scanf("%d %d\n", &N, &t);
    int A[N], most_common = 0, below_100 = 0;
    unordered_map<int,int> occurances; //{number: freq}
    for (int n = 0; n < N; n++) {
        scanf("%d", A+n);
        if (A[n] < 100) below_100++;
        occurances[A[n]]++;
        if (occurances.size() == 1 || occurances[A[n]] > occurances[most_common]) // check .size()==1 to prevent accidental initialisation of occurances[0]
            most_common = A[n];
    }
    sort(A,A+N);
    //
    switch (t) {
    case 1: { // go up and down the sorted list.
        int front = 0, back = N-1;
        while (1) {
            if (front == back) break;
            if (A[front]+A[back] > 7777) back--;
            else if (A[front]+A[back] < 7777) front++;
            else break;
        }
        if (front == back) printf("No");
        else printf("Yes");
        break;
    } case 2: // just check set size
        printf(occurances.size() == N ? "Unique" : "Contains duplicate");
        break;
    case 3: // occurances
        if (occurances[most_common] > N/2) printf("%d", most_common);
        else printf("%d", -1);
        break;
    case 4: // use a sorted array
        if (N%2) printf("%d", A[N/2]);
        else printf("%d %d", A[N/2-1], A[N/2]);
        break;
    case 5: // sorted array
        while (below_100 < N && A[below_100++] < 1000)
            printf(below_100<N && A[below_100]<1000 ? "%d " : "%d" , A[below_100-1]);
        break;
    }
    putchar(10);
}
