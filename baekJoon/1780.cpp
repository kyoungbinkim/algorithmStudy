#include <iostream>
#include <stdlib.h>

using namespace std;
int ans[3];

bool isTrue(int** arr, int x, int y, int n){
    int a = arr[x][y];
    for(int i=x ; i<x+n; i++)
        for (int j=y; j<y+n; j++)
            if(arr[i][j] != a)
                return false;
    ans[a+1] += 1;
    return true;
}

void update(int** arr, int x, int y, int n){
    if(isTrue(arr,x,y,n))
        return;
    int s = int(n/3);
    for(int i=0; i<3; i++)
        for(int j=0; j<3; j++)
            update(arr, x+i*s, y+j*s, s);
    return;
}

int main(){
    long int n;
    int** arr;
    cin >> n;
    
    arr = (int**)malloc(sizeof(int*)*n);
    for (int i=0; i<n; i++)
        arr[i] = (int*)malloc(sizeof(int)*n);   
    
    for(int i=0; i<n;i++)
        for(int j=0; j<n; j++)
            cin >> arr[i][j];
    update(arr, 0,0,n);

    for(int i=0; i<3; i++)
        cout << ans[i] << endl;
    
    return 0;
}