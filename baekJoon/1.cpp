#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    int N, C, W;
    int length[51] = {0,};
    int max = 0, sum, tmp;
    int cut_cnt;

    scanf("%d %d %d", &N, &C, &W);
    for (int i = 0; i < N; i++)
        scanf("%d", &length[i]);
    //제일 짧은 길이 -- 1까지 잘라서 계산해보고 가장 높은 값 출력

    sort(length, length + N);

    for (int i = length[N - 1]; i > 0; i--){
        sum = 0;
        for (int j = 0; j < N; j++){
            cut_cnt = (length[j]%i == 0) ? (length[j]/i - 1) : length[j]/i; //
            tmp = ((int)(length[j] / i)) * i * W - C * cut_cnt;//
            sum = tmp > 0 ? sum+tmp : sum; //
        }
        if (max <= sum)
            max = sum;
    }

    printf("%d\n", max);
    
    return 0;`
}