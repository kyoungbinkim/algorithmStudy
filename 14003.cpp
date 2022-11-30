#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, cnt;
vector<int> a, ans;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);	cout.tie(0);

	a.push_back(-1000000001);
	ans.push_back(-1000000001);
	cin >> n;
	for(int i = 0; i < n; i++) {
		int x;
		cin >> x;
		if(a.back() < x) {
			a.push_back(x);
			int check = 0, j;
			for(j = cnt; j >= 1; j--) {
				if(a[j] != ans[j])	check++;
				else	break;
			}
			for(int k = j; k <= cnt; k++) {
				ans[k] = a[k];
			}
			ans.push_back(x);
			cnt++;
		}
		else if(a.back() > x) {
			vector<int>::iterator idx = lower_bound(a.begin(), a.end(), x);
			*idx = x;
		}
	}
	cout << cnt << "\n";
	for(int i = 1; i <= cnt; i++) {
		cout << ans[i] << " ";
	}
	cout << "\n";
	return 0;
}
