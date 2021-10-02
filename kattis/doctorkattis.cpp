#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    map<int,map<int,string>> catQueue; // {infectionLevel: {time: catName}}
    unordered_map<string,pair<int,int>> catInfo;
    for (int n = 0; n < N; n++) {
        int cmd; cin >> cmd;
        string catName;
        short infectionLevel, updatedLevel;
        int time;
        switch (cmd) {
            case 0: //arrival
                cin >> catName >> infectionLevel;
                catInfo[catQueue[infectionLevel][n]=catName] = {infectionLevel,n};
                break;
            case 1: //update
                cin >> catName >> updatedLevel;
                tie(infectionLevel,time) = catInfo[catName];
                catQueue[infectionLevel].erase(time);
                if (!catQueue[infectionLevel].size()) catQueue.erase(infectionLevel);
                catQueue[catInfo[catName].first+=updatedLevel][time] = catName;
                break;
            case 2: //remove
                cin >> catName;
                tie(infectionLevel,time) = catInfo[catName];
                catQueue[infectionLevel].erase(time);
                if (!catQueue[infectionLevel].size()) catQueue.erase(infectionLevel);
                catInfo.erase(catName);
                break;
            case 3: //query
                if (!catQueue.size()) cout << "The clinic is empty\n";
                else cout << catQueue.rbegin()->second.begin()->second << endl;
                break;
        }
    }
}
