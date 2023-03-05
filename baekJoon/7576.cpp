#include <iostream>
<<<<<<< HEAD
=======
#include <stdlib.h>
>>>>>>> f685eb5 (update 2023.3.5)
#include <string>

using namespace std;

<<<<<<< HEAD
int main(){
    int col, row;
=======
bool check(int** arr, int row, int col){
    for(int i=0; i<row; i++){
        for(int j=0 ; j<col; j++)
            if(arr[i][j] == 0)
                return false;
    }
    return true;
}

bool update(int** arr, int row, int col, int dep){
    bool flag = false;
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            if(arr[i][j] != dep)
                continue;
            
            for(int x=-1 ; x<=1; x++){
                for(int y=-1; y<=1; y++){
                    if(x*y == 0 ){
                        if(i+x >=0 && i+x < row && j+y>=0 && j+y <col)
                            if(arr[i+x][j+y] == 0){
                                arr[i+x][j+y] = dep+1;
                                flag = true;
                            }
                    }
                }
            }
        }
    }
    return flag;
}

void printArr(int** arr, int row, int col){
    for(int i=0; i<row ; i++){
        for(int j=0; j<col ;j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
    return;
}

int main(){
    bool flag=true;
    int col, row, tmp, ans=1;
>>>>>>> f685eb5 (update 2023.3.5)
    int **arr;
    cin >> col >> row;
    arr= (int **)malloc(sizeof(int*) * row);
    for(int i=0; i<row; i++)
        arr[i] = (int*)malloc(sizeof(int) * col);
    
<<<<<<< HEAD
    for(int i=0; i<row ; i++)
        cout << arr[i] << endl;
    
=======
    for(int i=0; i<row; i++)
        for(int j=0; j<col; j++){
            cin >> tmp;
            arr[i][j] = tmp;
        }    

    while(flag){
        flag = update(arr, row, col, ans++);
    }

    if(check(arr,row,col))
        cout<< ans-2 <<endl;
    else
        cout << -1 << endl;
>>>>>>> f685eb5 (update 2023.3.5)
    return 0;
}

