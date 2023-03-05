#include <iostream>
#include <algorithm>
#include <map>

typedef long long uInt;
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    uInt num, n, tmp;
    cin >> num;
    for(int i=0; i<num ;i++){
        map<uInt,uInt> size2n;
        cin >> n; 
        double th = (double)n/2;
        bool flag = true;
        for(int j=0; j<n; j++){
            cin >> tmp;
            size2n[tmp]++;
            if (size2n[tmp] > th && flag){
                cout <<tmp << '\n';
                flag = false;
            }
        }
        if(flag) { cout << "SYJKGW\n";}
    }


    return 0;
}