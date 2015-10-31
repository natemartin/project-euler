#include "sudoku.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
  std::ifstream input("sudoku.txt");
  std::string line;
  int count = 0;
  int total = 0;
  while(input >> line) {
    input >> line;
    int soln[9][9];
    int grid[9][9];
    for(int i = 0; i < 9; i++) {
      input >> line;
      cout << line << endl;
      for(int j = 0; j < 9; j++) {
        grid[i][j] = line[j] - 48;
      }
    }
    Sudoku sudoku(grid);
    sudoku.Solve(soln);
    total += (soln[0][0] * 100 + soln[0][1] * 10 + soln[0][2]);
    cout << "Solved " << count++ << endl;
  }
  cout << "Total " << total << endl;
}
