#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

map<int, vector<int> > factor_cache;

vector<int> GetFactors(int x) {
  vector<int> factors;
  for(int i = 2; i < x + 1; ++i) {
    bool added = false;
    while(x % i == 0) {
      x/=i;
      if(!added) {
        factors.push_back(i);
        added = true;
      }
    }
  }
  return factors;
}


int main() {

}
