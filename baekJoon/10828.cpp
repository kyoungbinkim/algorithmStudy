#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

class stack{
    int pos;
    int data[10000];
public:
    stack(){
        pos = 0;
    }
    void push(int n){
        data[pos++] = n;
    }
    int pop(){
        if(pos == 0) return -1;
        return data[--this->pos];
    }
    int size(){
        return pos;
    }
    int empty(){
        return (pos==0);
    }
    int top(){
        if(pos ==0) return -1;
        return data[pos-1];
    }
};

int main(){
    string cmd;
    int n;
    stack s;
    int cmdNum;
    cin >> cmdNum;
    for(int i=0; i<cmdNum; i++){
        cin >> cmd;
        if (!cmd.compare("push")) {
            cin >> n;
            s.push(n);
        }   
        else if(!cmd.compare("pop")){cout << s.pop() << endl;}
        else if(!cmd.compare("empty")){cout<<1*s.empty()<<endl;}
        else if(!cmd.compare("top")){cout << s.top() << endl;}
        else if(!cmd.compare("size")){cout << s.size() << endl;}
    }
    return 0;
}