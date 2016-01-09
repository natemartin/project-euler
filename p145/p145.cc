#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

inline bool IsReversable(int x) {
  string rev_x = std::to_string(x);
  std::reverse(rev_x.begin(), rev_x.end());
  if (rev_x[0] == '0') {
    return false;
  }
  int sum = stoi(rev_x) + x;
  string sum_str = std::to_string(sum);

  std::size_t found = sum_str.find("0");
  if (found!=std::string::npos)
    return false;
  found = sum_str.find("2");
  if (found!=std::string::npos)
    return false;
  found = sum_str.find("4");
  if (found!=std::string::npos)
    return false;
  found = sum_str.find("6");
  if (found!=std::string::npos)
    return false;
  found = sum_str.find("8");
  if (found!=std::string::npos)
    return false;
  return true;
}

int main() {
  int count = 0;
  for (int i = 1; i < 1000000000; i++) {
    if (IsReversable(i)) {
      count++;
    }
    if (i % 10000000 == 0) {
      cout << i << endl;
    }

  }
  std::cout << count << std::endl;
}
