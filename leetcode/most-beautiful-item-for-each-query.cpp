// I don't like using cpp, but its implementation of ordered maps is most familiar. 
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        map<int,int> most_beautiful;
        most_beautiful[0] = 0;
        sort(items.begin(), items.end());
        for (auto &item: items) {
            int maxb = most_beautiful.rbegin()->second;
            most_beautiful[item[0]] = max(maxb, item[1]);
        }
        vector<int> ans;
        for (auto &q: queries) {
            auto it = most_beautiful.upper_bound(q);
            it--;
            ans.push_back(it->second);
        }
        return ans;
    }
};
int main() {
    Solution s;
    vector<vector<int>> a1 = {{1,2},{3,2},{2,4},{5,6},{3,5}};
    vector<int> a2 = {1,2,3,4,5,6};
    for (auto &u: s.maximumBeauty(a1, a2)) {
        cout << u << " ";
    }
    puts("");
    vector<vector<int>> b1 = {{10,1000}};
    vector<int> b2 = {5};
    for (auto &u: s.maximumBeauty(b1, b2)) {
        cout << u << " ";
    }
}
