#include <iostream>
using namespace std;

int main(){
    int vacationDay,  kSize, mSize;
    int k,m;
    int kday, mday;
    cin >> vacationDay >> kSize >> mSize >>k >> m;
    kday = int(kSize/k);
    mday = int(mSize/m);
    if (kSize %k != 0) kday++;
    if (mSize %m != 0) mday++;

    if (mday>kday) {
        cout << vacationDay-mday <<endl;
    }
    else {
        cout << vacationDay-kday <<endl;
    }
}