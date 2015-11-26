#include <iostream>
#include <set>

using namespace std;

typedef unsigned long long uint64 ;

int main() {
  set<uint64> pent;
  set<uint64> hex;

  for(uint64 i = 1; i < 1000000; i++) {
    hex.insert(i * (2*i - 1));
    pent.insert((i * (3*i - 1)) / 2);
    uint64 tri = (i * (i+1)) / 2;
    // triangular series is lower bounded by the pentagonal and hexagonal series.
    if (pent.find(tri) != pent.end() && hex.find(tri) != hex.end()) {
      cout << tri << endl;
      if (tri > 40755) break;
    }
  }
}
