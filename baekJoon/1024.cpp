#include <iostream>

using namespace std;
typedef long long bigint;

int main(){
    bigint n,l,start;
    bool flag = false;
    cin >> n >> l;

    while(1){
        if(l>100){
            cout << "-1\n";
            break;
        }
        else if(l%2 == 1 && n%l == 0){
            start = (bigint)(n/l) - (bigint)l/2;
            if (start <0) {l++;continue;}
            flag = true;
            break;
        }
        else if (l%2 == 0 && ( n - (bigint)l/2 ) % l == 0){
            start = (bigint)(n/l) - (bigint)l/2 + 1;
            if (start <0) {l++;continue;}
            flag = true;
            break;
        }
        l++;
    }
    if(flag){
        bigint end = (bigint)n/l + (bigint)l/2;
        for(bigint i=start; i<=end; i++)
            cout << i << " ";
        cout << "\n";
    }
    return 0;
}