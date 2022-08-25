#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
// using namespace stdext;

class user {
    string name;
    int *reporterInd;
    int reportedNum;
public:
    user(string n, int size){
        name = n; 
        reportedNum =0;
        reporterInd = new int [size];
    }
    string getName(){return name;}
    int getReportedNum(){ return reportedNum; }
    void reported(int from){reportedNum++;}
};


class Report{
    map<string, int> static name2ind;
    int static **r;
    int size;
public:
    Report(){}
    Report(string r){
        
    }
    
    void clear(int size);
    void update(string r);
    
    int** &getReports(){return r;}
    int getInd(string n){
        return name2ind.at(n);
    }
    map<string, int>& getMap(){
        return name2ind;
    }
    int getColumnSum(int i);
    
};

void Report::clear(int size){
    this->size = size;
    for (int i=0 ; i<size; i++)
        for (int j=0; j<size; j++)
            r[i][j] = 0;
}

void Report::update(string r){
    string from,to;
    int fromInd, toInd;
    
    // cout << r.find(" ") <<endl;
    from = r.substr(0,r.find(" "));
    to = r.substr(r.find(" ")+1 , r.size()-r.find(" ")-1);
    
    fromInd = name2ind.at(from);
    toInd = name2ind.at(to);
    
    
    // cout <<fromInd << toInd << endl;
    this->r[fromInd][toInd] = 1;
}

int Report::getColumnSum(int i){
    int result = 0;
    for (int j=0; j<size; j++){
        result += r[j][i];
    }
    return result;
}

int** Report::r;
map <string, int> Report::name2ind;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer; 
    Report r;
    r.getReports() = new int*[id_list.size()];
    for (int i=0; i< id_list.size(); i++){
        r.getReports()[i] = new int[id_list.size()];
    }
    r.clear(id_list.size());
    
    
    for (int i=0; i< id_list.size(); i++){
        // cout << id_list[i] << endl;
        r.getMap().insert({id_list[i], i});
    }
    for (int i=0 ; i<report.size(); i++){
        r.update(report[i]);
    }
    
    int* tmp = new int [id_list.size()];
    int** myr = r.getReports();
    
    for (int i=0; i<id_list.size(); i++)
        tmp[i] = 0;
    
    
    for (int i=0; i<id_list.size(); i++){
        if(r.getColumnSum(i) >= k){
            // tmp[i]+=1;
            for(int j=0; j<id_list.size();j++){
                if(myr[j][i] >=1){
                    tmp[j]+=1;
                }
            }
        }
    }
    for (int i=0 ; i<id_list.size(); i++)
        answer.push_back(tmp[i]);
    
    
    return answer;
}