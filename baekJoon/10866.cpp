#include <iostream>
#include <string>
#include <vector>

using namespace std;

class deck{
    vector<int> deck;
public:
    void printDeck(){
        for(int i=0; i<deck.size(); i++)
            cout << deck[i] << " ";
        cout << endl;
    }
    int empty(){
        return deck.empty()*1;
    }
    void push_front(int n){
        deck.insert(deck.begin(), n);
    }
    void push_back(int n){
        deck.push_back(n);
    }
    int pop_front(){
        if (this->empty()) return -1;
        int tmp = deck.at(0);
        deck.erase(deck.begin());
        return tmp;
    }
    int pop_back(){
        if (this->empty()) return -1;
        int tmp = deck.back();
        deck.pop_back();
        return tmp;
    }
    int size(){
        return deck.size();
    }
    int front(){
        if (this->empty()) return -1;
        return deck.front();
    }
    int back(){
        if (this->empty()) return -1;
        return deck.back();
    }

};

int main(){
    deck d;
    int cmdNum, n;
    cin >> cmdNum;

    string cmd;
    for(int i=0; i<cmdNum; i++){
        cin >> cmd;
        if (cmd == "push_front"){
            cin >> n;
            d.push_front(n);
        }
        else if (cmd == "push_back"){
            cin >> n;
            d.push_back(n);
        }
        else if (cmd == "pop_front"){
            cout << d.pop_front() << endl;
        }
        else if (cmd == "pop_back"){
            cout << d.pop_back() << endl;
        }
        else if (cmd == "size"){
            cout << d.size() << endl;
        }
        else if (cmd == "empty")
            cout << d.empty() << endl;

        else if (cmd == "front")
            cout<< d.front() << endl;
        else if (cmd == "back")
            cout << d.back() << endl;
    }

    return 0;
}
