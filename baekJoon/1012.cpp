#include<iostream>
#include<stdlib.h>
#include<queue>

using namespace std;

void BFS(int **arr,int w, int h, int cnt, int r, int c){
    queue<pair<int,int>> q; q.push(make_pair(r,c));
    int x,y;
    
    while(q.size() > 0){
        y = q.front().first;
        x = q.front().second;

        int dx[] = {0, -1, 1, 0};
        int dy[] = {-1, 0, 0, 1};
        arr[y][x] = cnt;

        for(int i=0; i<4; i++){
            if (x+dx[i] <0 || x+dx[i] >= w || y+dy[i]<0 || y+dy[i]>=h) continue;
            if (arr[y+dy[i]][x+dx[i]] == 1) {
                q.push(make_pair(y+dy[i],x+dx[i]));
                arr[y+dy[i]][x+dx[i]] = cnt;
            }
        }

        // for(int i=-1; i<=1 ;i++){
        //     for(int j=-1; j<=1; j++)
        //     {
        //         if (j*i != 0 || i+j ==0) continue;
        //         if (x+i <0 || x+i >= w || y+j<0 || y+j>=h) continue;
        //         if (arr[y+j][x+i] == 1) {
        //             q.push(make_pair(y+j,x+i));
        //             arr[y+j][x+i] = cnt;
        //         }
        //     }
        // }
        q.pop();
    }
    
}

void printArr(int**arr, int h, int w){
    for(int i=0; i<h;i++){
        for (int j=0; j<w; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
    cout << endl;
}

int main(){
    ios::sync_with_stdio(false);
    int t; cin >> t;
    int **arr;

    int w,h,n;
    int row, col;
    for (int it=0; it<t; it++){
        cin >>w >> h >> n;
        arr = (int **) malloc ( sizeof(int *) * h);
        arr[0] = (int *) malloc ( sizeof(int) * w*h );
        for( int i=1; i<h; i++){
            arr[i] = arr[ i-1 ] + w;
        }

        for(row=0; row<h; row++)
            for(col=0; col<w; col ++)
                arr[row][col] = 0;
        for(int i=0; i<n; i++){
            cin >> col>>row;
            arr[row][col] = 1;
        }
        // printArr(arr,h,w);

        int ans = 2;
        for(row=0; row<h; row++){
            for(col=0; col<w; col ++){
                if(arr[row][col] == 1){
                    BFS(arr, w, h, ans++, row, col);
                    // printArr(arr,h,w);
                }
            }
        }
        cout << ans-2<<endl;
        free(arr[0]);
        free(arr);
    }

    return 0;
}