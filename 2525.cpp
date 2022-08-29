#include <iostream>
using namespace std;

int main(){
    int hour,min;
    int C, sumMin;
    cin >> hour >> min;
    cin >> C;
    sumMin = (hour*60 + min + C) % 1440;
    cout << int(sumMin/60) << " " << sumMin%60 <<endl;
}