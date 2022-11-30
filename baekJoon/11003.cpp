#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    vector<int> numVec, ans;

    int n, l, tmp, before;
    scanf("%d %d", &n, &l);
    for (int i=0; i<n; i++){
        scanf("%d ", &tmp);
        numVec.push_back(tmp);
    }
    ans.push_back(numVec[0]);
    for (int i=1; i<l; i++){
        ans.push_back(min(ans[i-1], numVec[i]));
    }

    for (int i=l; i<n; i++){
        before = ans[i-1];
        if (numVec[i] <= before){
            ans.push_back(numVec[i]); continue;
        }
        else if (numVec[i-l] == before){
            ans.push_back(*min_element(numVec.begin()+i-l+1, numVec.begin()+i+1));
        }
        else{
            ans.push_back(before);
        }
    }

    for(vector<int>::iterator it=ans.begin(); it!=ans.end(); it++){
        printf("%d ", *it);
    }
    printf("\n");

    return 0;
}