#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);

    int size, i, *arr;
    vector<int> dval;
    cin >> size;
    arr = (int*)malloc((size+1)* sizeof(int));

    arr[0]=0; dval.push_back(0);
    for(i=1;i<=size;i++)
        cin >> arr[i];

    for(i=1; i<=size; i++){
        int val = arr[i];
        // cout<< "dval back : " << dval.back() << endl;
        // cout << "val : " << val << endl<< (dval.back()<val) << endl << endl;
        if(dval.back() < val){
            dval.push_back(val);
        }
        else{
            int lo=0, hi=dval.size()-1;
            int mid = (lo+hi)/2;

            while (lo<=hi){
                if(val > dval[mid]){
                    lo = mid+1;
                }
                else{
                    hi = mid-1;
                }
                mid = (lo+hi)/2;
            }
            // cout<< "low : "<< lo << " "<< dval[lo]<< endl;
            // cout<< "hig : "<< hi << " "<< dval[hi]<< endl;
            *(dval.begin()+lo) = val;
            // cout<<endl;
        }
    }

    cout << dval.size()-1 << endl;;

    free(arr);
    return 0;
}