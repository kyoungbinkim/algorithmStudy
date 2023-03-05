#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    vector<long long> treelen;
    long long n,c,w,tmp;

    cin>>n>>c>>w;
    for(int i=0;i<n;i++){
        cin >> tmp; treelen.push_back(tmp);
    }
    sort(treelen.begin(), treelen.end());
    long long ans = 0, cut_len=1, sumTmp =0;
    int cut_num, cut_tree_num, maxVal = treelen.back();

    while(1){
        sumTmp = 0;
        for(int i=0; i<n; i++){

            cut_num = (treelen[i]%cut_len == 0) ? treelen[i]/cut_len - 1 : treelen[i]/cut_len;
            cut_tree_num = treelen[i] / cut_len;
            // cout <<cut_len<< " " << treelen[i]<<" " << cut_num <<cut_tree_num << endl;
            tmp = cut_len*cut_tree_num*w - cut_num*c;
            sumTmp += ((tmp>0)? tmp : 0);
        }
        // cout << "sumTmp : " << sumTmp << endl << endl;
        if( sumTmp > ans){ans= sumTmp;}
        if( cut_len > maxVal) break;
        cut_len++;
    }
    cout<< ans<< endl;
    
    
    return 0;
}
