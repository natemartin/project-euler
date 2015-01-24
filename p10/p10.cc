#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main() {
  vector<int> primes;
  primes.push_back(2);
  for(int i = 3; i < 2000000; i+=2) {
    for(int j : primes) {
      if(i % j == 0) break;
      if((float) j > sqrt(i)) {
        primes.push_back(i);
        break;
      }
    }
  }

  long sum = 0;
  for(int i : primes) {
    sum += i;
  }
  cout << sum << endl;
}
