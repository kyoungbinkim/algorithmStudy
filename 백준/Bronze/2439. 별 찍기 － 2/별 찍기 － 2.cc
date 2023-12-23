#include <iostream>
using namespace std;
void printChar(char c, int num){
    for (int i=0; i<num; i++)
        cout << c;
}
int main(){
    int size;
    cin >> size;
    for (int i=1; i<=size; i++){
        printChar(' ', size-i);
        printChar('*', i);
        cout<<endl;
    }
}