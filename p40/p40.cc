#include <iostream>
#include <string>

using namespace std;

int main() {

  string dec = "";
  for(int i = 1; i < 1000000; i++) {
    dec.append(to_string(i));
  };
  int product = 1;
  product*= (dec[0] - '0');
  product*= (dec[9] - '0');
  product*= (dec[99] - '0');
  product*= (dec[999] - '0');
  product*= (dec[9999] - '0');
  product*= (dec[99999] - '0');
  product*= (dec[999999] - '0');
  cout << product << endl;

}
