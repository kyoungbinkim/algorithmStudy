#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

typedef unsigned long long B8;

void updatePrimeList(B8* plist, B8 endsqrt){
    for(int i=2; i<=endsqrt; i++)
        plist[i] = i;

    for(int i=0; i<= endsqrt; i++){
        if (plist[i]==0) continue;

        for (int j=2*i; j<=endsqrt; j+=i)
            plist[j] = 0;
    }
}

B8 updateAnsList(int* ans,B8* plist, B8 start, B8 end, B8 plistSize){
    B8 Sum = 0;
    int ansSize = end - start + 1;
    for(int i=0; i<ansSize; i++)
        ans[i] = 1;
    
    for(int i=0; i<plistSize; i++){
        if(!plist[i]) continue;
        B8 primeSquare = plist[i]*plist[i];

        for(B8 j = ceil(start/primeSquare); j<= B8(end/primeSquare); j++){
            if (j*primeSquare - start<ansSize)
                ans[j*primeSquare - start] = 0;
        }
    }

    for(int i=0; i<ansSize; i++){
        Sum += ans[i];
    }
    return Sum;
}

int main(){
    B8 start, end, endsqrt, *plist, tmp;
    int* ansArr;
    cin >> start >> end;
    endsqrt = B8(sqrt(end))+1;

    plist = (B8*)malloc(sizeof(B8) * (endsqrt+1));
    ansArr = (int*)malloc(sizeof(int) * (end-start+1));

    updatePrimeList(plist, endsqrt);
    
    tmp = updateAnsList(ansArr, plist, start, end, endsqrt+1);
    cout<< tmp <<endl;
    return 0;
}
