#include <iostream>
using namespace std;

int main() {
  int first = 1;
  int second = 1;
  int sum = 0;
  while(second <= 4000000) {
    int temp = first + second;
    if(temp % 2 == 0) {
      sum+=temp;
    }
    first = second;
    second = temp;
  }
  std::cout << sum << endl;
}
