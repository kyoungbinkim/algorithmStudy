#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

void arrCopy(int** dest, int** f, int vecSize){
    for(int i=0; i<vecSize; i++){
        dest[i][0] = f[i][0];
        dest[i][1] = f[i][1];
    }
}

double vectorMatch(int** veclist, int start, int dep, int tar, int vecSize){
    if(dep == tar){
        int Sum[2] = {0,0};
        for (int i=0; i<vecSize; i++){
            Sum[0] += veclist[i][0];
            Sum[1] += veclist[i][1];
        }
        return sqrt(Sum[0]*Sum[0] + Sum[1]*Sum[1]);
    }
    // for(int i=0; i<vecSize; i++)
    //     cout << veclist[i][0] << " "<< veclist[i][1] <<", ";
    // cout << endl;

    int ansSize = vecSize+dep-tar-start+1;
    double *ans;
    ans = (double*)malloc(sizeof(double) * ansSize);
    int **tmp;
    tmp = (int**)malloc(sizeof(int*) * vecSize);
    for(int i=0; i<vecSize; i++)
        tmp[i] = (int*)malloc(sizeof(int)*2);
    for(int i=start; i<= vecSize+dep-tar; i++){
        arrCopy(tmp, veclist, vecSize);
        tmp[i][0] = -tmp[i][0];
        tmp[i][1] = -tmp[i][1];
        ans[i-start] = vectorMatch(tmp, i+1, dep+1, tar, vecSize);
    }
    double k = 1000000000;
    cout <<endl;
    for (int i=0; i<ansSize; i++){
        cout << ans[i] << "  ";
        if (k>ans[i])
            k = ans[i];
    }
    cout << endl << endl;
    return k;
}

int main(){
    int iter;
    cin >> iter;
    for(int i=0; i<iter; i++){
        int vecSize, **vecList;
        cin >> vecSize;
        vecList = (int**)malloc(sizeof(int*) * vecSize);
        for (int j=0;j<vecSize; j++)
            vecList[j] =(int*)malloc(sizeof(int)*2);
        
        for(int j=0 ; j<vecSize; j++)
            cin >> vecList[j][0] >> vecList[j][1];
        cout << "ans : "<<vectorMatch(vecList, 0, 0, int(vecSize/2), vecSize) << endl;
    }
    return 0;
}