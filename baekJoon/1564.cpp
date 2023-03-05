#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int n; cin >> n;

    unsigned long long ans = 1;

    for(int cnt=1; cnt<=n; cnt++){
        ans = ans * cnt;
        while(ans %10 ==0) {ans = ans/10;}
        ans = ans % (unsigned long long)pow10(12);
    }
    ans = ans % (unsigned long long)pow10(5);
    cout.width(5); cout.fill('0');
    cout << ans << endl;
}