#include <iostream>
using namespace std;

int main(){
    long long b1=0, b2=1, ans;
    long long n;
    cin >> n;

    for(long long i=2; i<=n; i++){
        ans = (b1+b2) % 1000000007;
        b1 = b2;
        b2 = ans;
    }
    if(n==0)
        ans = 0;
    else if(n==1)
        ans = 1;
    cout << ans <<endl;
    return 0;
}