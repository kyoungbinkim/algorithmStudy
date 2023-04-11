#include <iostream>
#include <vector>

using namespace std;
int ans[400][400] = {0,};
vector<int>  graph[400];
int visit[400] = {0,};

void update(int start, int i){
    for(vector<int>::iterator it= graph[i].begin(); it != graph[i].end(); it++){
        ans[start][*it] = -1;
        ans[*it][start] = 1;
        update(start, *it);
    }
}


int main(){
    ios::sync_with_stdio(false);
    int n, k, s, e, num;
    cin >> n >> k;

    for(int i=0; i<k; i++){
        cin >> s >> e;
        graph[s-1].push_back(e-1);
    }

    for(int i=0; i<n; i++)
        update(i,i);

    cin >> num;

    for(int i=0; i<num; i++){
        cin >> s >> e;
        cout << ans[s-1][e-1]<< '\n';
    }

    return 0;
}