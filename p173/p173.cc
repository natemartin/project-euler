#include <iostream>

using namespace std;

int main() {
  int total_laminae = 0;
  for(int i = 2; i < 1000; i++) {
    auto current_ring = i;
    int remaining_tiles = 1000000;
    while (remaining_tiles > 0) {
      remaining_tiles -= (current_ring * 4);
      if (remaining_tiles >= 0) {
        total_laminae++;
        current_ring+=2;
      } else
        break;
    }
  }
  cout << total_laminae << endl;
}
