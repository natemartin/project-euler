#include "sudoku.h"

#include <set>
#include <iostream>

using namespace std;

Sudoku::Sudoku(int grid[9][9]) {
  squares_remaining = 81;
  for(int i = 0; i < 9; i++) {
    for(int j = 0; j < 9; j++) {
      if (grid[i][j] >= 1 && grid[i][j] <= 9) {
        grid_[i][j] = grid[i][j];
        squares_remaining--;
      } else {
        grid_[i][j] = 0;
      }
    }
  }
}
void Sudoku::PrintGrid() {
  for(int i = 0; i < 9; i++) {
    for(int j = 0; j < 9; j++) {
      cout << grid_[i][j];
    }
    cout << endl;
  }
}

// Attempt to solve the puzzle with the following strategy.
// Whenever possible, fill in the squares based on standard elimination rules.
// When there are no more squares to fill, start guessing. Backtrack whenever a
// guess leads to no possible moves.
bool Sudoku::Solve(int (&result)[9][9]) {
  bool elim_failed = false;
  while (squares_remaining > 0) {
    bool result = AttemptElimFill();
    if (!result) {
      elim_failed = true;
      break;
    }
  }
  if (elim_failed) {
    // Check if this board is consistent i.e. all squares have at least one possible value
    int soln[9][9];
    for(int i = 0; i < 9; i++) {
      for(int j = 0; j < 9; j++) {
        if (grid_[i][j] == 0) {
          auto vals = GetPossibleValues(i,j);
          for(auto val : vals) {
            grid_[i][j] = val;
            Sudoku temp(grid_);
            bool test = temp.Solve(result);
            if (test) {
              return true;
            }
          }
          return false;
        }
      }
    }
  }
  for(int i = 0; i < 9; i++) {
    for(int j = 0; j < 9; j++) {
      cout << grid_[i][j];
      result[i][j] = grid_[i][j];
    }
    cout << endl;
  }
  return true;
}

void Sudoku::GetRow(int (&row)[9], int row_num) {
  for(int i = 0; i < 9; i++) {
    row[i] = grid_[row_num][i];
  }
}

void Sudoku::GetCol(int (&col)[9], int col_num) {
  for(int i = 0; i < 9; i++) {
    col[i] = grid_[i][col_num];
  }
}

void Sudoku::GetBox(int (&box)[9], int x, int y) {
  int start_row, start_col;
  if (x < 3) {
    start_row = 0;
  } else if (x < 6) {
    start_row = 3;
  } else {
    start_row = 6;
  }

  if (y < 3) {
    start_col = 0;
  } else if (y < 6) {
    start_col = 3;
  } else {
    start_col = 6;
  }

  int pos = 0;
  for(int i = 0; i < 3; i++) {
    for(int j = 0; j < 3; j++) {
      box[pos++] = grid_[i + start_row][j + start_col];
    }
  }

}

set<int> Sudoku::GetPossibleValues(int x, int y) {
  set<int> possible_vals;
  for(int i : vals) {
    possible_vals.insert(i);
  }
  int row[9], col[9], box[9];
  GetRow(row, x);
  GetCol(col, y);
  GetBox(box, x, y);

  for(auto i : row) {
    possible_vals.erase(i);
  }
  for(auto i : col) {
    possible_vals.erase(i);
  }
  for(auto i : box) {
    possible_vals.erase(i);
  }
  return possible_vals;
}

bool Sudoku::AttemptElimFill() {
  for(int i = 0; i < 9; i++) {
    for(int j = 0; j < 9; j++) {
      if (grid_[i][j] == 0) {
        set<int> possible_vals = GetPossibleValues(i, j);
        if (possible_vals.size() == 1) {
          grid_[i][j] = *(possible_vals.begin());
          squares_remaining--;
          return true;
        }
      }
    }
  }
  return false;
}
