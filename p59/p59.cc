#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool test_for_english(vector<char>& input) {
  string input_string = "";
  for(char i : input) {
    input_string.append(1, i);
  }
  size_t found = input_string.find("Gospel");
  if (found!=string::npos) {
    cout << input_string << endl;
    return true;
  }

  return false;
}

int main() {

  vector<char> cipher;

  fstream myfile("cipher.txt", ios_base::in);
  string x;
  while (myfile.good())
  {
    getline(myfile, x, ',');
    cipher.push_back(atoi(x.c_str()));
  }
  for(char i = 'a'; i <= 'z'; i++) {
    for(char j = 'a'; j <= 'z'; j++) {
      for(char k = 'a'; k <= 'z'; k++) {
        vector<char> test;
        for(int a = 0; a < cipher.size(); a++) {
          if (a%3 == 0) {
            test.push_back(cipher[a] ^ i);
          } else if(a%3 == 1) {
            test.push_back(cipher[a] ^ j);
          } else {
            test.push_back(cipher[a] ^ k);
          }
        }
        if (test_for_english(test)) {
          int sum = 0;
          for(char x : test)
            sum += x;
          cout << sum << endl;
          exit(0);
        }
      }
    }
  }

}
