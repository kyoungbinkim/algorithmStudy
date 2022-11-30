#include <iostream>
#include <vector>

using namespace std;

class rotateQueue{
    vector<int> q;
public:

    rotateQueue(int size){
        for(int i=1; i<=size; i++){
            q.push_back(i);
        }
    }

    int search(int n){
        int size = q.size();
        int ind;

        for(int i=0; i<size; i++){
            if(q[i] == n){
                ind = i;
                break;
            }
        }
        // 0 1 2 3 
        int ans = (size-ind >= ind) ? ind : size-ind;
        if(ans == ind){
            for(int i=0; i<ans; i++)
                cmd2();
        }
        else{
            for(int i=0; i<ans; i++)
                cmd3();
        }
        cmd1();
        return ans;
    }

    int cmd1(){
        int ans = q.front();
        q.erase(q.begin());
        return ans;
    }

    void cmd2(){
        int ans = q.front();
        q.erase(q.begin());
        q.push_back(ans);
        return;
    }

    void cmd3(){
        int ans = q.back();
        q.insert(q.begin(), ans);
        q.pop_back();
        return;
    }

    void printQ(){
        for(int i=0; i<q.size(); i++)
            cout << q[i] << " ";
        cout <<"\n";
    }
};

int main(){
    int n,m, tmp, ans =0;
    cin >> n >> m;
    rotateQueue rq = rotateQueue(n);
    for(int i=0; i<m; i++){
        cin >> tmp;
        ans += rq.search(tmp);
        // rq.printQ();
        // cout << ans << endl << endl;
    }
    cout << ans << endl;
    return 0;
}