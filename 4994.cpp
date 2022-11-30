#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

string BFS(int n){
    vector<string> que;
    que.push_back("1");

    while(1){
        string tmp = que[0];
        que.erase(que.begin());

        que.push_back(tmp + "1");
        que.push_back(tmp + "0");

        if(stol(tmp) % n == 0) return tmp;
    }
}

int main(){
    int n;
    while (1)
    {
        cin >> n;
        if (!n) break;
        
        cout << BFS(n) << endl;
    }
    return 0;
}

