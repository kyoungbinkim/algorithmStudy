#include <iostream>
#include <stack>
#include <stdlib.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    stack<int> s;
    int ans = 0, size, tmp, m=0;

    cin >> size;
    int* arr = (int *)malloc(sizeof(int) * (size+1));
    int* ansArr = (int *)malloc(sizeof(int) * size); 
    
    for(int i=0; i<size; i++) {
        cin >> arr[i];
    }
        
    for(int i=size-1; i>=0; i--){
        if(arr[i] >= m){
            ansArr[i] = -1;
            m = arr[i];
            s.push(arr[i]);
            continue;
        }
        while(s.top() <= arr[i]){
            s.pop();
        }

        ansArr[i] = s.top();
        s.push(arr[i]);

    }

    for(int i=0; i<size; i++)
        cout << ansArr[i] << ' ';
    cout <<'\n';
    return 0;
}