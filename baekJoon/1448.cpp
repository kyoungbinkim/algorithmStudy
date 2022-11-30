#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int Get(int* wid, int start, int *ans, int dep, int l){
    if(dep == 3){
        int m = -1;
        int s = 0;
        for(int i=0; i <3; i++){
            s += ans[i];
            if (m< ans[i])
                m = ans[i];
        }
        if (m < s-m)
            return s;
        return -1;
    }

    int tmp = -1;
    for (int i=start; i<l; i++){
        ans[dep] = wid[i];
        int a = Get(wid, i+1, ans, dep+1, l);
        if (a>tmp)
            tmp = a;
    }
    return tmp;
}

int main(){
    int size;
    int ans[3] = {0,0,0};
    int *wid;

    cin >> size;
    wid = (int*)malloc(sizeof(int) * size);

    for(int i=0; i<size; i++)
        cin >> wid[i];

    cout << Get(wid, 0,ans, 0, size) << endl;

    return 0;
}