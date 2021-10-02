#include <bits/stdc++.h>
using namespace std;
#define Point pair<int,int>
struct Phash {
    size_t operator()(Point const& p) const noexcept {
        return hash<size_t>{}((((size_t)p.first)<<32)+p.second);
    }
};
const vector<vector<int>> FLYS = {{0,0,3}, {0,0,1}, {1,1,0}, {1,1,2}, {2,2,1}, {2,2,3}, {3,3,2}, {3,3,0}};
Point getPoint() {
    int x,y; scanf("%d %d", &x, &y);
    return {x,y};
}
inline Point flip(Point &p) { return {p.second, p.first}; }
Point* check_aligned(Point *ptr, Point p, bool flipped) {
    if (flipped) {
        if (ptr->second != p.first) return NULL;
    } else {
        if (ptr->first != p.first) return NULL;
    }
    return ptr;
}
int main() {
    int N; scanf("%d\n", &N);
    Point start = getPoint(), end = getPoint();
    // collect unblocked points; sort them
    Point unblocked[N];
    map<Point,int> sortbyX, sortbyY; // N*logN, but since N < 200000, this alone shouldn't be TLE 
    for (int n = 0; n < N; n++) {
        unblocked[n] = getPoint();
        sortbyX[unblocked[n]] = n;
        sortbyY[flip(unblocked[n])] = n;
    }
    // functions to collate the possible steps from a given point.
    unordered_map<Point*,Point*[4]> steps; // {Point: /*NESW*/ {Point, Point, Point, Point}}
    auto getPoint = [&] (map<Point,int> &origin, typeof(sortbyX.begin()) it, bool flipped, bool higher) -> Point* {
        Point p = it->first;
        if (higher) {
            if (++it == origin.end()) return NULL;
        } else {
            if (it-- == origin.begin()) return NULL;
        }
        return check_aligned(unblocked+it->second, p, flipped);
    };
    // get backreferences of {point:iterator} so that there's no need to pull O(logn) queries for every getSteps()
    unordered_map<Point,typeof(sortbyX.begin()),Phash> backrefX, backrefY;
    auto getSteps = [&] (Point *cur) {
        if (!steps.count(cur)) {
            if (!backrefX.count(*cur)) {
                auto itx = sortbyX.lower_bound(*cur), ity = sortbyY.lower_bound(flip(*cur)); //this is logn
                backrefX[itx->first] = itx; backrefY[ity->first] = ity;
            }
            auto itx = backrefX[*cur], ity = backrefY[flip(*cur)]; //otherwise O(k)
            steps[cur][0] = getPoint(sortbyX, itx, 0, 1);
            steps[cur][1] = getPoint(sortbyY, ity, 1, 1);
            steps[cur][2] = getPoint(sortbyX, itx, 0, 0);
            steps[cur][3] = getPoint(sortbyY, ity, 1, 0);
        }
        return steps[cur];
    };
    // do an as-lazy-as-possible BFS
    vector<Point> *border = new vector<Point>(); border->push_back(start);
    unordered_set<Point, Phash> seen;
    int i = 0;
    while (!border->empty()) {
        vector<Point> *newb = new vector<Point>();
        for (auto &cur: *border) {
            if (seen.count(cur)) // oops
                continue;
            if (cur == end) {
                printf("%d\n", i);
                return 0;
            }
            seen.insert(cur);
            // generate adjacencies on the fly
            Point *cur_ptr = unblocked+sortbyX[cur];
            for (auto &fly: FLYS) {
                Point *tmp = cur_ptr;
                for (auto &dir: fly) {
                    if (getSteps(tmp)[dir]) tmp = getSteps(tmp)[dir];
                    else {
                        tmp = NULL; break;
                    }
                }
                if (tmp) newb->push_back(*tmp);
            }
        }
        delete border;
        border = newb;
        i++;
    }
    printf("%d\n", -1);
}
