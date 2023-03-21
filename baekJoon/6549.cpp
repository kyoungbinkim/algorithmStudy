#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stack>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);

    int arr[100001] ={0,};
    
    while(1){
        
        int size,tmp,h=0;
        cin >> size;
        
        stack<int> s;
        if(size == 0) break;

        // int * arr= (int *)malloc(sizeof(int) * size);
        for(int i=0;i<size; i++) cin >> arr[i];
        long long ans=arr[0];

        for(int i=0; i<size; i++){
            // if(arr[i]!=0 && (s.size()==0 || arr[s.top()] < arr[i])){
            //     s.push(i);
            // }else{
                cout << i <<' ' << h << endl;
                if(0<h && h<=arr[i]){
                    ans += h;
                    cout << "'hi'2  "<<h << "\t" << ans <<endl;
                }
                else{
                    h=0;
                }

                while(s.size() && arr[s.top()]>arr[i]){
                    tmp = s.top(); s.pop();
                    if((long long)arr[tmp] * (i-tmp) > ans ){
                        ans = (long long)arr[tmp] *(long long) (i-tmp);
                        cout << ans << ' '<< arr[tmp] << endl;
                        h=arr[tmp];
                    }

                    else{
                        h=0;
                    }
                    
                    // ans = (long long)arr[tmp] * (i-tmp) > ans ? (long long)arr[tmp] * (i-tmp) : ans;
                }
            // }
            if(s.size() ==0){
                ans = (long long)arr[i] * (i+1) > ans ? (long long)arr[i] * (i+1) : ans;
                cout << "'hi'" << ans <<endl;
            }
            s.push(i);
        }

        long long ans2=0;
        while(!s.empty()){
            tmp = s.top(); s.pop();
            if(!s.empty()){
                ans2 = (long long)arr[tmp] * (tmp-s.top()) > ans2 ? (long long)arr[tmp] * (tmp-s.top()) : ans2;
            }
            if(s.size()== 0){
                cout << ans << ' ' << tmp<< endl;
                ans = max( (long long)size * arr[tmp], ans);
            }
            ans2 = (long long)arr[tmp] * (size-tmp) > ans2 ? (long long)arr[tmp] * (size-tmp) : ans2;
        }
        cout << max(ans, ans2) << '\n';
    }
    

    return 0;
}