#include <bits/stdc++.h>
using namespace std;

int n;
string commands;
int r = 1, c = 1;

int dr[4] = {0, 0, -1, 1};
int dc[4] = {1, -1, 0, 0};
char console[4] = {'R', 'L', 'U', 'D'};

int main(void) {
    freopen("input.txt", "r", stdin);
    cin >> n;
    cin.ignore();
    getline(cin, commands);

    for (int i = 0; i < commands.size(); i++) {
        char command = commands[i];
        int nr = -1, nc = -1;
        for (int j = 0; j < 4; j++) {
            if (command == console[j]) {
                nr = r + dr[j];
                nc = c + dc[j];
            }
        }
        if (nr < 1 || nc < 1 || nr > n || nc > n) continue;
        r = nr;
        c = nc;
    }
    cout << r << ' ' << c << '\n';
    return 0;
}
