#include <iostream>
#include <string>
using namespace std;

int main(){
    int n,m;
    string fish;
    cin >>n >>m;
    for (int i=0; i<n; i++){
        cin >> fish;
        for (int j=m-1; j>=0; j--) cout << fish[j];
        cout <<endl;
    }
}