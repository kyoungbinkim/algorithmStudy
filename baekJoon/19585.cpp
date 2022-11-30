#include <iostream>
#include <iomanip>
#include <functional>
#include <string>
#include <vector>
#include <map>

using namespace std;

struct node {
    char key;
    map<char, node> child;
    bool flag;
};

void print_node(node n){
    cout << n.key << " " << n.flag << endl;
    for(map<char,node>::iterator it=n.child.begin(); it != n.child.end(); it++){
        cout << it->first << " ";
    } cout << endl;
}

class Trie{
    node rt;
public:
    void update(string s){
        node *current = &rt;

        for(int i=0; i<s.size(); i++){
            if(current->child.find(s[i]) == current->child.end()){
                node tmp; tmp.key = s[i]; tmp.flag=false;
                current->child.insert(make_pair(s[i], tmp));
                // print_node(tmp);
            }
            current = &(current->child[s[i]]);
        }
        current->flag = true;
        return;
    }

    int search(string s){
        node *current = &rt;

        for(int i=0; i<s.size(); i++){
            if(current->child.find(s[i]) == current->child.end()) return 0;
            current = &(current->child[s[i]]);
        }
        return current->flag;
    }
};

int main(){
    ios::sync_with_stdio(false);

    int c,n,q;
    string tmp, tmp2;
    vector<string> color, name;
    Trie trie;
    cin >> c >> n;

    for (int i=0; i<c; i++){
        cin >> tmp;
        color.push_back(tmp);
    }

    for(int i=0; i<n; i++){
        cin >> tmp;
        name.push_back(tmp);
    }
    
    hash<string> myhash;
    for(vector<string>::iterator it=color.begin(); it!=color.end(); it++){
        tmp = *it;
        for(vector<string>::iterator jt=name.begin(); jt!=name.end(); jt++){
            trie.update(to_string(myhash(tmp + *jt)));
        }
    } 

    name.clear(); color.clear();

    cin >> q;
    for(int i=0; i<q; i++){
        cin >> tmp;
        if(trie.search(to_string(myhash(tmp)))){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }

    return 0;
}
