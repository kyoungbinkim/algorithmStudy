#include <iostream>

using namespace std;

int main(){
    int n;
    int wid =2;
    cin >> n;
    for (int i=0; i<n ; i++){
        wid = wid*2-1; // 2 3 5 9  17
    }
    cout << wid*wid << endl;
}