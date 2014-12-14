#include <iostream>
using namespace std;

bool isPythTrip(int a, int b, int c) {
  if(a > b && a > c) {
    return a*a == b*b + c*c;
  }
  if(b > a && b > c) {
    return b*b == a*a + c*c;
  }
  if(c > b && c > a) {
    return c*c == b*b + a*a;
  }
  return false;
}

int main() {
  for(int i = 0; i < 1000; i++) {
    for(int j = 0; j < 1000; j++) {
      int k = 1000 - i - j;
      if(isPythTrip(i,j,k)) {
        cout << i * j * k << endl;
        return 0;
      }
    }
  }
}

