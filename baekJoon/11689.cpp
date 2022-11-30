#include <iostream>
#include <math.h>
#include <map>
#include <stdlib.h>

using namespace std;
typedef unsigned long long U64;

bool isPrime(U64 n){
    if(n==2 || n==3)
        return true;
    else if(n%2 ==0 || n==1)
        return false;
    
    for(U64 i=3; i<U64(sqrtl(n)+1) ; i+=2){
        if (n%i == 0) return false;
    }
    return true;
}

int main(){
    map<U64, int> factor;

    U64 d = 2;
    U64 x ,ans = 1;
    cin >> x;
    if(isPrime(x)){
        cout << x-1 <<endl;
        return 0;
    }
    while(d<= x){
        if(x%d == 0){
            if(factor.find(d) == factor.end()){
                factor[d] = 1;
            }
            else{
                factor[d]++;
            }
            x = x/d;
            if (isPrime(x)){
                factor[x]++;
                break;
            }
        }
        else{
            d++;
        }
    }

    for(auto i=factor.begin(); i!=factor.end(); i++){
        // cout << i->first << " " << i->second << endl;

        ans = ans * U64(powl(i->first, i->second-1)) * (i->first-1);
    }

    cout << ans <<endl;
    return 0;
}