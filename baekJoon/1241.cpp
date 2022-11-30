#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <math.h>

using namespace std;


set<int> getDivisor(int n){
    int dist = sqrt(n)+1;
    set<int> ans;
    for(int i=1; i<=dist; i++){
        if(n%i == 0){
            ans.insert(n/i);
            ans.insert(i);
        }
    }

    return ans;
}

int main(){
    long long ans;
    int n,tmp; cin >> n;
    vector<int> numVec;
    map<int, int>Map;
    set<int> k;
    for(int i=0; i<n; i++){
        scanf("%d", &tmp);
        Map[tmp]++; 
        numVec.push_back(tmp);
    }
    for(vector<int>::iterator it=numVec.begin(); it!=numVec.end(); it++){
        ans = -1;
        k = getDivisor(*it);

        for(set<int>::iterator jt=k.begin(); jt!=k.end(); jt++){
            if (Map.find(*jt) != Map.end())
                ans += Map[*jt];
        }
        printf("%lld\n", ans);
    }

    return 0;
}