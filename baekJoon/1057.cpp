#include <iostream>

using namespace std;

int main(){
    int torSize, a,b,ans=0;
    cin >> torSize >> a >> b;
    a--; b--;
    while(a!=b){
        torSize = (torSize%2 == 0) ? torSize/2: torSize/2+1;
        a= a/2; b=b/2; ans++;
    }

    cout << ans << endl;

    return 0;
}