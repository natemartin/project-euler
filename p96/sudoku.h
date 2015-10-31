#include <set>

class Sudoku {
 public:
  Sudoku(int grid[9][9]);
  bool Solve(int (&result)[9][9]);
 private:
  void PrintGrid();
  bool AttemptElimFill();
  void GetRow(int (&row)[9], int row_num);
  void GetCol(int (&col)[9], int col_num);
  void GetBox(int (&box)[9], int x, int y);
  std::set<int> GetPossibleValues(int x, int y);
  int grid_[9][9];
  int squares_remaining;
  int vals[9] = {1,2,3,4,5,6,7,8,9};
};
