#include <iostream>
#include <map>
#include <unordered_map>
using namespace std;
#define num 1000
int main() {
  unordered_map<int,unordered_map<int,unsigned long long> > results;
  for(int i = 1; i < num; i++) {
    auto& res_i = results[i];
    for(int j = 1; j <= i; j++) {
      if (j == 1) {
        res_i[j] = 1;
      } else if(i == j) {
        res_i[j] = 1 + res_i[j-1];
        cout << res_i[j] << endl;
        if (res_i[j] % 1000000 == 0) {
          cout << i << endl;
        }
      } else {
        if ((i-j) < j) {
          res_i[j] = results[i-j][i-j] + res_i[j-1];
        } else {
          res_i[j] = results[i-j][j] + res_i[j-1];
        }
      }
    }
  }
  cout << results[5][5] << endl;
}
