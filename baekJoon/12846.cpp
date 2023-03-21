#include <iostream>
#include <stdlib.h>
#include <stack>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);

    stack<int> s;
    int size,ans=0,tmp;
    cin >> size;

    int * arr= (int *)malloc(sizeof(int) * size);
    for(int i=0;i<size; i++) cin >> arr[i];

    for(int i=0; i<size; i++){
        if(s.size()==0 || arr[s.top()] < arr[i]){
            s.push(i);
        }else{
            while(s.size() > 1 && arr[s.top()]>arr[i]){
                tmp = s.top(); s.pop();
                ans = arr[tmp] * (i-tmp) > ans ? arr[tmp] * (i-tmp) : ans;
            }
        }
        
    }
    cout << ans << endl;

    return 0;
}