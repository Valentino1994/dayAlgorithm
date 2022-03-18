#include <bits/stdc++.h>
using namespace std;
int n;
int m;  
string s;
int a[10][10];
int main() {
    freopen("input.txt", "r", stdin);
    cin >> n >> m;
    for(int i = 0; i <= n; i++) {
        getline(cin, s);
        cout << s << "\n";
    }

    return 0;
}