#include <iostream>
#include <string>

using namespace std;

int main(){
    int col, row;
    int **arr;
    cin >> col >> row;
    arr= (int **)malloc(sizeof(int*) * row);
    for(int i=0; i<row; i++)
        arr[i] = (int*)malloc(sizeof(int) * col);
    
    for(int i=0; i<row ; i++)
        cout << arr[i] << endl;
    
    return 0;
}

