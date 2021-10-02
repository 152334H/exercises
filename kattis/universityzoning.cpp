#include <bits/stdc++.h>
using namespace std;
#define Point pair<int,int>
struct Phash {
    size_t operator()(Point const& p) const noexcept {
        return hash<size_t>{}((((size_t)p.first)<<32)+p.second);
    }
};
Point getPoint() {
    int y,x;
    scanf("%d %d", &y, &x);
    return {y,x};
}
struct Student {
    Point pos;
    int num;
    int fac;
};
struct Faculty {
    set<Point> zone;
    int Target;
    set<int> SID; // student IDs
};
int mhat_dist(Point p, Point t) {
    return abs(p.first-t.first) + abs(p.second-t.second);
}
int main() {
    int R, C, F, S, G; scanf("%d %d %d %d %d\n", &R, &C, &F, &S, &G);
    Faculty faculty[F+1];
    unordered_map<int,Student> student;
    for (int i = 1; i <= F; i++) {
        short K; scanf("%d", &K);
        for (int k = 0; k < K; k++)
            faculty[i].zone.insert(getPoint());
    }
    for (int i = 0; i < S; i++) {
        Point loc = getPoint();
        int D, f; scanf("%d %d", &D, &f);
        student[D] = {loc, D, f};
        faculty[f].SID.insert(D);
    }
    for (int i = 1; i <= F; i++)
        scanf("%d", &faculty[i].Target);
    // for every faculty, generate the steps required for each student. Sort to find the minimum steps needed.
    long long mini[F] = {0};
    for (int f = 1; f <= F; f++) {
        auto &fac = faculty[f];
        vector<int> steps;
        auto itz = fac.zone.begin();
        for (auto its = fac.SID.begin(); its != fac.SID.end(); itz++,its++)
            steps.push_back(mhat_dist(student[*its].pos, *itz));
        sort(steps.begin(), steps.end());
        for (int i = 0; i < fac.Target; i++) mini[f-1] += steps[i];
    }
    // then sort the list of minimum steps required.
    sort(mini, mini+F);
    long long total = 0;
    for (int i = 0; i < G; i++) total += mini[i];
    printf("%lld\n", total); // hopefully I dont need to switch to pqueues to prevent TLE
}
