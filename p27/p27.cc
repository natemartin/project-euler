#include <iostream>
#include <vector>
#include <set>
#include <math.h>
using namespace std;

vector<int> primes;
set<int> prime_set;

void GenPrimes() {
  primes.push_back(2);
  for (int i = 3; i < 10000000; i+=2) {
    for (auto j : primes) {
      if( i % j == 0) {
        break;
      }
      if( j > sqrt(i) ) {
        primes.push_back(i);
        break;
      }
    }
  }
}

int CheckQuad(int a, int b) {
  for(int i = 0;;i++) {
    int result = i*i + a*i + b;
    if(prime_set.count(result) < 1) {
      return i;
    }
  }
}

int main() {
  GenPrimes();
  for(auto prime : primes) {
    prime_set.insert(prime);
  }
  int max_a;
  int max_b;
  int max_run = 0;
  for(int i = -999; i < 1000; i++) {
    for(int j = -999; j < 1000; j++) {
      int result = CheckQuad(i, j);
      if(result > max_run) {
        max_a = i;
        max_b = j;
        max_run = result;
      }
    }
  }
  cout << max_a * max_b << endl;
}
