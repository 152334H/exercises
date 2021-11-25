// last ditch attempt to get a working solution
// cpp beacuse it has sorted maps
// still fails
#include <bits/stdc++.h>
using namespace std;
/*
def NSE(arr: list):
    n =len(arr)
    s = []
    mp = {}
    s.append(arr[0])
    for i in range(1, n):
        if (len(s) == 0):
            s.append(arr[i])
            continue
        while (len(s) != 0 and s[-1] > arr[i]):
            mp[s[-1]] = i
            s.pop()
        s.append(arr[i])
 
    while (len(s) != 0):
        mp[s[-1]] = None
        s.pop()
    return {arr[i]: mp[arr[i]] for i in range(n)}
*/
map<int, int> NSE(vector<int> arr)
{
    int n = arr.size();
    vector<int> s;
    map<int, int> mp;
    s.push_back(arr[0]);
    for (int i = 1; i < n; i++)
    {
        if (s.size() == 0)
        {
            s.push_back(arr[i]);
            continue;
        }
        while (s.size() != 0 and s[s.size() - 1] > arr[i])
        {
            mp[s[s.size() - 1]] = i;
            s.pop_back();
        }
        s.push_back(arr[i]);
    }
    while (s.size() != 0)
    {
        mp[s[s.size() - 1]] = -1;
        s.pop_back();
    }
    return mp;
}
/*
for t in range(int(input())):
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    '''A subsequence a[i:j] is considered valid if and only if
    min(a[i:k] for k in range(i+1,j)) >= -s
    Find the largest possible contiguous subsequence.'''
    sat = [0]*(n+1)
    for i in range(n): sat[i+1] = sat[i] + a[i]
    next_smallest_index = NSE(sat,s)
    #
    ans = 0
    best = None
    for i in range(n):
        j = next_smallest_index[sat[i]]
        if j is None: j = n
        else:
            assert sat[j]+s < sat[i]
            j -= 1
        if j-i > ans:
            ans = j-i
            best = (i,j)
    if best is None: print(-1)
    else: print(' '.join(map(str,[best[0]+1,best[1]])))
*/
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, s;
        cin >> n >> s;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        vector<int> sat(n + 1);
        for (int i = 0; i < n; i++) {
            sat[i + 1] = sat[i] + a[i];
        }
        vector<int> sat_copy;
        for (auto &i: sat) { sat_copy.push_back(i+s); }
        map<int, int> next_smallest_index = NSE(sat_copy);
        /*
        bool nonneg_seen = false;
        int prev = -1;
        for (auto it = next_smallest_index.rbegin(); it != next_smallest_index.rend(); it++) {
            if (it->second != -1) nonneg_seen = true;
            if (it->second == -1 && nonneg_seen) {
                next_smallest_index[it->first] = prev;
            }
            prev = it->second;
        }*/
        int ans = 0;
        pair<int, int> best;
        for (int i = 0; i < n; i++) {
            int j = next_smallest_index.lower_bound(sat[i])->second;
            if (j == -1) {
                j = n;
            } else {
                assert(sat[j] + s < sat[i]);
                j--;
            }
            if (j - i > ans) {
                ans = j - i;
                best = {i, j};
            }
        }
        if (best.first == -1) {
            cout << -1 << endl;
        } else {
            cout << best.first + 1 << " " << best.second << endl;
        }
    }
    return 0;
}
