#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main(){
    int iter;
    cin >> iter;
    for(int i=0; i<iter; i++){
        int vecSize, **vecList;
        cin >> vecSize;
        vecList = (int**)malloc(sizeof(int*) * vecSize);
        for (int j=0;j<vecSize; j++)
            vecList[i] =(int*)malloc(sizeof(int)*2);
        
        for(int i=0 ; i<vecSize; i++)
            cin >> vecList[i][0] >> vecList[i][1];

    }
    return 0;
}