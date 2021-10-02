#include <bits/stdc++.h>
using namespace std;
int main() {
    int T; scanf("%d\n", &T);
    for (int t = 0, c, end=1; t < T; t++, putchar(10)) {
        deque<char> line, tmp;
        while ((c = getchar()) != '\n') {
            switch (c) {
            case '<':
                if (end && line.size()) line.pop_back();
                else if (!end && tmp.size()) tmp.pop_front();
                break;
            case '[':
                end = 0;
                for (auto c: tmp) line.push_front(c);
                tmp.clear();
                break;
            case ']':
                end = 1;
                for (auto c: tmp) line.push_front(c);
                tmp.clear();
                break;
            default:
                if (end) line.push_back(c);
                else tmp.push_front(c);
            }
        }
        for (auto c: tmp) line.push_front(c);
        tmp.clear();
        for (auto c: line) putchar(c);
    }
}
