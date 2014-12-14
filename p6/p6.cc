#include <iostream>
using namespace std;

int main() {
  long long sumSquares = 0;
  long long squareSums = 0;
  for(int i = 1; i <=100; i++) {
    squareSums+=i;
    sumSquares += i*i;
  }
  squareSums*=squareSums;
  cout << squareSums - sumSquares << endl;
}

