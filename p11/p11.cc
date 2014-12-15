#include <iostream>
#include <fstream>

using namespace std;

int main() {

  string filename = "matrix.txt";
  ifstream infile(filename);

  int matrix[20][20];
  for(int i = 0; i < 20; i++) {
    for(int j = 0; j < 20; j++) {
      infile >> matrix[i][j];
    }
  }

  int maxProduct = 0;
  for(int i = 0; i < 20; i++) {
    for(int j = 0; j < 20; j++) {
      int product;
      if(i < 17) {
        product = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j];
        if(product > maxProduct) {
          maxProduct = product;
        }
      }
      if(j < 17) {
        product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3];
        if(product > maxProduct) {
          maxProduct = product;
        }
      }
      if(i < 17 && j > 2) {
        product = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3];
        if(product > maxProduct) {
          maxProduct = product;
        }
      }
      if(i < 17 && j < 17) {
        product = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3];
        if(product > maxProduct) {
          maxProduct = product;
        }
      }
    }
  }
  cout << maxProduct << endl;
}
