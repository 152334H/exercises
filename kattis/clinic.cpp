#include <bits/stdc++.h>
using namespace std;
#define Patient pair<long long,string>
struct lesser {
    constexpr bool operator()(const Patient &lhs, const Patient &rhs) const {
        return lhs.first == rhs.first ? lhs.second > rhs.second : lhs.first < rhs.first;
    }
};
int main() {
    int N, K; scanf("%d %d\n", &N, &K);
    priority_queue<Patient,vector<Patient>,lesser> clinic; // not sure if the sorting here will work out.
    unordered_set<string> dying, died;
    for (int n = 0; n < N; n++) {
        int T, S; char M[12];
        switch (getchar()) {
        case '1':
            scanf(" %d %s %d\n", &T, M, &S);
            clinic.push({S-(long long)K*(long long)T, M});
            dying.insert(M);
            break;
        case '2': {
            scanf(" %d\n", &T);
            Patient cured = {0, ""};
            do {
                if (clinic.empty()) break;
                cured = clinic.top();
                clinic.pop();
            } while (died.count(cured.second));
            if (cured.second == "" || died.count(cured.second)) puts("doctor takes a break");
            else {
                dying.erase(cured.second);
                cout << cured.second << '\n';
            }
            break;}
        case '3':
            scanf(" %d %s\n", &T, M);
            if (dying.count(M)) {
                dying.erase(M);
                died.insert(M);
            }
            break;
        }
    }
}
