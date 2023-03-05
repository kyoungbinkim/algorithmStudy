#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <set>

using namespace std;

bool check(set<float> tmp, float*arr, int size){
    for(int i=0; i<size; i++){
        if(tmp.find(arr[i]) == tmp.end())
            return false;
    }
    return true;
}

void printSet(set<float> tmp){
    for(auto it=tmp.begin(); it!=tmp.end(); it++)
        cout << *it << " ";
    cout << endl;
}

int main(){
    int size;
    float arr[50];
    set<float> tmp;
    cin >> size;
    for(int i=0; i<size; i++)
        cin>> arr[i];
    
    long ans = 1;

    while (1)
    {   
        tmp.clear();
        for(int s=0; s<=ans*10; s++){
            tmp.insert(floor(((double)s* 1000)/ans)/1000);
        }
        if(check(tmp, arr, size))
            break;
        // printSet(tmp);
        ans++;
    }
    cout << ans <<endl;
    return 0;
}