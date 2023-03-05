#include<iostream>
#include<string>
#include<math.h>

using namespace std;

class bigInt{
    unsigned long long val[10];
    int size;  
public:
    bigInt(string s){
        size = (s.length() % 10 ==0) ? s.length()/10 : s.length()/10+1; 
        // cout << "len : " << s.length() << " size : "<< size << endl;
        for(int i=0; i<size-1; i++){
            // cout << s.substr(s.length()- (i+1)*10, 10) <<" ";
            val[i] =stoull(s.substr((s.length()- (i+1)*10), 10));
            // cout << val[i] << " " << s <<endl;
        }
        val[size-1] = stoull(s.substr(0, (s.length()%10 == 0) ? 10: s.length()%10));
        // cout << val[size-1] <<endl;
    }

    void calc()
    {
        int carry = 0;
        for(int i=0; i<size; i++){
            val[i] = val[i] * 2 + carry;

            if(val[i] >= pow10(10) && i<size-1){
                cout <<"event !" << val[i] <<endl;
                carry = 1;
                val[i] = val[i] % (unsigned long long)pow10(10);
                cout <<"event !" << val[i] <<endl;
            }
            else{carry = 0;}
        }
        
        int i=0;
        do{ 
            if (val[i] == 0){
                val[i] = (unsigned long long)pow10(10) - 1;
            }
            else {val[i]-=1;}
        }while(val[i++]==(unsigned long long)pow10(10) - 1);	
        
        i=0;
        do{ 
            if (val[i] == 0){
                val[i] = (unsigned long long)pow10(10) - 1;
            }
            else {val[i]-=1;}
        }while(val[i++]==(unsigned long long)pow10(10) - 1);	
        
        cout << val[size-1];
        for(i=size-2; i>=0; i--){
            cout.width(10);
            cout.fill('0');
            cout << val[i];
        }
        cout <<endl;
    }

};
int main(){
    string n;
    cin >> n;
    if(n=="1") {
        cout << 1<<endl;
        return 0;
    }
    bigInt ans = bigInt(n);
    ans.calc();
    return 0;
}