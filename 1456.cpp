#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool isPrime(long long n){
    if(n==2 || n==3)
        return true;
    else if (n%2==0 || n==1)
        return false;
    
    for (uint64_t i=3; i <  uint64_t(sqrtl(n)+1); i+=2){
        if(n%i == 0)
            return false;
    }
    return true;
}

long long nextPrime(long long n){
    if(n==2)
        return 3;
    long long tmp = n+1;
    while(!isPrime(tmp))
        tmp+=2;
    return tmp;
}

int main(){
    long ans = 0, n;
    long long a,b;
    cin >> a >> b;
    n = nextPrime(1);
    long tar = long(sqrt(b)+1);
    
    while(n<tar){
        long long tmp = n*n;
        while(tmp<=b){
            if(tmp >= a)
                ans += 1;
            tmp = tmp * n;
        }
        n = nextPrime(n);
    }
    cout << ans << endl;

    return 0;
}