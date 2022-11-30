#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int size,tmp;
    cin >> size;
    vector<int> arr;
    for(int i=0; i<size; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }

    // ind ans
    queue< pair<int, int> > q;
    int visit[10000] = {0,};
    int start,end;
    cin >> start >> end; start--; end--;
    q.push(pair<int,int>(start, 0)); visit[start]=1;

    pair<int,int> p;
    while(q.size() > 0){
        p = q.front(); 

        if(abs(end - p.first) % arr[p.first] == 0){
            cout << p.second + 1 << endl;
            return 0;
        }

        for(int i=p.first%arr[p.first]; i<size; i+= arr[p.first])
            if (visit[i] == 0){
                q.push(pair<int,int>(i,p.second+1));
                visit[i] = 1;
            }

        q.pop();
        
    }

    cout << -1 << endl;

    return 0;
}
