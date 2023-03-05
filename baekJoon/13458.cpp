#include <iostream>
#include <cmath>

using namespace std;
#define CALC(a) ((a)<0) ? 0 : (a)
int main(){
    ios::sync_with_stdio(false);
    int size, a[1000000],b,c;
    unsigned long long ans = 0;
    cin >> size;

    for(int i=0; i<size; i++)
        cin >> a[i];
    cin >> b >> c;
    for(int i=0; i<size; i++)
        ans +=(unsigned long long) (1+ceil(CALC(a[i]-b) / (float)c));

    cout << ans <<endl;

    return 0;
}