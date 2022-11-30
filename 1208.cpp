#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int size,i, tar, *nlist;
    map<int, int> ansMap;

    cin >> size >> tar;
    nlist = (int *)malloc(size * sizeof(int));
    for(i=0; i<size; i++)
        cin >> nlist[i];

    return 0;
}