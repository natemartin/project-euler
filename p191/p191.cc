#include <iostream>
#include <string>
#include <queue>

using namespace std;
int main() {
  int limit = 30;
  long long total = 0;
  queue<string> queue;
  queue.push("");
  while (queue.size() > 0) {
    auto current = queue.front();
    queue.pop();
    if (current.size() == limit) {
      total += 1 + count(current.begin(), current.end(), 'O');
      continue;
    }
    queue.push(current + "O");
    if (current.size() < 2 or !(current[current.size() - 1] == 'A' && current[current.size() - 2] == 'A')) {
      queue.push(current + "A");
    }
  }
  cout << total << endl;
}
