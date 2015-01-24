#include <iostream>
using namespace std;

int numDivisors(long input) {
  int num = 0;
  for(int i = 1; i <= input / 2 + 1; i++) {
    if(input % i == 0) num++;
  }
  return num;
}

int main() {
  long currentTriNum = 0;
  for(int i = 1; i < 10002; i++) {
    currentTriNum+=i;
    /* int result = numDivisors(currentTriNum); */
    /* cout << currentTriNum << " - " << result << endl; */
    /* if(result > 500) exit(0); */
  }
  cout << currentTriNum << " - " << numDivisors(currentTriNum) << endl;
}
