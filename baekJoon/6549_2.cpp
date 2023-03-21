#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

int main()
{

    long long arr[100001] = {
        0,
    };

    stack<long long> s;
    int size;
    long long ans = 0, tmp, hi, wid;

    cin >> size;

    for (int i = 0; i < size; i++)
        cin >> arr[i];

    for (int i = 0; i < size; i++)
    {
        while (!s.empty() && arr[s.top()] >= arr[i])
        {
            hi = arr[s.top()];
            s.pop();
            wid = s.empty() ? i : i - 1 - s.top();

            ans = max(hi * wid, ans);

            // s.pop();
        }
        s.push(i);
    }
    while (!s.empty())
    {
        hi = arr[s.top()];
        s.pop();
        wid = s.empty() ? size : size - 1 - s.top();

        ans = max(hi * wid, ans);
    }
    cout << ans << '\n';

    return 0;
}