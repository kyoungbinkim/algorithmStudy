#include <iostream>
#include <string>
using namespace std;

int main(){
    int num;
    int min5=300, min1=60, sec10=10;
    cin >> num;
    if (num%10 != 0){
        cout << -1 <<endl;
        return 0;
    }
    
    cout << int(num/min5) << " ";
    num = num % min5;

    cout << int(num/min1) <<" ";
    num = num % min1;

    cout << int(num/sec10) << endl;
    return 0;
}