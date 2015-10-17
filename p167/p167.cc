#include <set>
#include <queue>
#include <iostream>

using namespace std;

typedef unsigned long long int uint64;

uint64 Ulam(uint64 a, uint64 b, uint64 k) {
  set<uint64> ulam_sequence;
  set<uint64> blacklist;
  queue<uint64> nums;
  nums.push(a+b);
  ulam_sequence.insert(a);
  ulam_sequence.insert(b);
  auto last_inserted = b;
  while(ulam_sequence.size() < k) {
    auto i = nums.front();
    nums.pop();
    if ( ulam_sequence.find(i) != ulam_sequence.end() ) {
      ulam_sequence.erase(i);
      blacklist.insert(i);
      continue;
    }
    if ( blacklist.find(i) != blacklist.end() ) {
      continue;
    }
    for(auto j : ulam_sequence) {
      nums.push(i + j);
    }
    ulam_sequence.insert(i);
    last_inserted = i;
  }

  return last_inserted;
}

int main() {
  cout << Ulam(1, 2, 5) << endl;
}
