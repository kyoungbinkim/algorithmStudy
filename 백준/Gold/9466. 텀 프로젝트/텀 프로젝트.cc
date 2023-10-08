#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main(){
    ios::sync_with_stdio(false);

    int n, size;
    int student[100001];
    cin >> n;

    for(int x=0 ; x<n ; x++){
        cin >> size;

        unordered_set<int> visit, ansVisit;

        for(int i=1; i<=size; i++) { cin >> student[i]; }

        for(int i=1; i<= size; i++){
            if(visit.find(i) != visit.end()) continue;

            vector<int> log= {i};
            unordered_set<int> logVisit= {i};
            int next = student[i];

            while(logVisit.find(next) == logVisit.end() && visit.find(next) == visit.end()){
                log.push_back(next);
                logVisit.insert(next);
                next = student[next];
            }

            
            if (logVisit.find(next) != logVisit.end()){
                bool FLAG = false;

                for(int idx=0; idx<log.size(); idx++){
                    if(log[idx] == next) FLAG = true;
                    if(FLAG) {
                        ansVisit.insert(log[idx]);
                    }
                }
            }
            visit.merge(logVisit);
        }
        // cout << ansVisit << endl;
        cout << size - ansVisit.size() << '\n';
    }

    return 0;
}