#include <bits/stdc++.h>
using namespace std;
deque<int> teque[2];
int tqsize;
int main() {
    int N; scanf("%d\n", &N);
    for (int n = 0; n < N; n++) {
        char cmd[16]; scanf("%s", cmd);
        int i; scanf("%d\n", &i);
        if (*cmd == 'g') { // get
            if (i < teque[0].size()) printf("%d\n", teque[0][i]);
            else printf("%d\n", teque[1][i-teque[0].size()]);
        } else { // push_*
            tqsize++;
            switch (cmd[5]) {
            case 'b':
                teque[1].push_back(i);
                break;
            case 'f':
                teque[0].push_front(i);
                break;
            case 'm': // forcibly balance deques until an insertion at teque[0].back is where push_middle should go
                while (teque[0].size() < tqsize/2) {
                    int tmp = teque[1].front();
                    teque[1].pop_front();
                    teque[0].push_back(tmp);
                }
                while (teque[0].size() > tqsize/2) {
                    int tmp = teque[0].back();
                    teque[0].pop_back();
                    teque[1].push_front(tmp);
                }
                teque[0].push_back(i);
                break;
            }
        }
    }
}
