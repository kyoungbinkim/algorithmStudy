#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);

    int size, arr1[50], arr2[50], ans = 0;
    cin >> size;
    
    for(int i=0; i<size; i++)
        cin >> arr1[i];
    for(int i=0; i<size; i++)
        cin >> arr2[i];

    sort(arr1, arr1+size);
    sort(arr2, arr2+size);

    for(int i=0; i<size; i++){
        ans += arr1[i] * arr2[size-i-1];
    }
    cout << ans <<endl;
    
    

    

    return 0;
}