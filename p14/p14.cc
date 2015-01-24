#include <iostream>
using namespace std;

long collatzLength(long start) {
  int repCount = 0;
  while(start != 1) {
    if(start % 2 == 0) {
      start/=2;
    } else {
      start = start * 3 + 1;
    }
    repCount++;
  }
  return repCount;
}

int main() {
  int highestLen = 1;
  int highestStart = 1;
  for(long i = 2; i < 1000000; i++) {
    long temp = collatzLength(i);
    if(temp > highestLen) {
      highestLen = temp;
      highestStart = i;
    }
  }
  cout << highestStart << endl;
}
