#include<bits/stdc++.h>
using namespace std;
int ret = 1;
void a() {
  ret = 2;
  cout << ret << "\n";
  return ;
}

double b() {
  return 1.2333;
}

int main() {
  a();
  double ret = b();
  char c = 'c';
  string d = "wow fantastic";
  string e = "wow";
  e += " ";
  e += "wonderful";

  cout << ret << "\n";
  cout << c << "\n";
  cout << d << "\n";
  cout << e.size() << "\n";
  cout << e << "\n";
  
  return 0;
}
