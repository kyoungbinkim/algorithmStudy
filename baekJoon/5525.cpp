#include <iostream>
#include <string>

using namespace std;

int main(){
    int n, slen, ans=0, j;
    string s;
    cin >> n >> slen >> s;

    for(int i=0; i<slen-2*n; i++){
        if(s[i]=='O')
            continue;
        
        for(j=0; j<2*n; j++){
            if(s[i+j] == s[i+j+1])
                break;
        }
        if(j == 2*n)
            ans++;
    }
    cout << ans <<endl;
    return 0;
}