#include <iostream>
#include <stdlib.h>

using namespace std;


class myQ{
    int *q, size;
public:
    myQ(int n){
        q = (int *)malloc(n * sizeof(int));
        for(int i=0; i<n; i++) q[i] = i;
        this->size = n;
    }  

    int findNum(int target){
        for(int i=0; i<size ; i++)
            if(target == q[i])
                return i;
        return -1;
    }

    int popAnd

    int calc(int target){
        int ind = findNum(target);

    }


};


int main(){
    int qSize, n;
    


    return 0;
}