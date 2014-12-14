#include <iostream>
using namespace std;

bool checkPalindrome(int input) {
  std::string s = std::to_string(input);
  for(int i = 0; i < s.length(); i++) {
    if(s[i] != s[s.length() - 1 - i]) return false;
  }
  return true;
}

int main() {
  int biggest = 0;
  for(int i = 100; i < 1000; i++) {
    for(int j = 100; j < 1000; j++) {
      if(checkPalindrome(i*j)) {
        if(i * j > biggest) {
          biggest = i*j;
        }
      }
    }
  }
  cout << biggest << endl;
}

