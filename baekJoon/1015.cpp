#include <iostream>

using namespace std;

int main(){
    int size,i,j;
    int arr[51], ans[51];
    cin >> size;
    for(i=0;i<size; i++)
        cin >> arr[i];
    
    int ind = 0;
    for(i=1; i<=1000; i++)
        for(j=0; j<size; j++)
            if(arr[j] == i)
                ans[j] = ind++;

    for(i=0; i<size; i++)
        cout << ans[i] << " ";
    cout << endl;

    return 0;
}