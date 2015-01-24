#include <iostream>
#include <vector>
using namespace std;

class BBS {
    long current;
  public:
    BBS(long seed);
    int getNext();
};

BBS::BBS(long seed) {
  current = seed;
}

int BBS::getNext() {
  current = (current * current) % 50515093;
  int answer = current % 500;
  return answer;
}

class LineSegment {
    int p1x, p1y, p2x, p2y;
  public:
    LineSegment(int a, int b, int c, int d);
    bool testIntersection(LineSegment otherLine);
};

LineSegment::LineSegment(int a, int b, int c, int d) {
  p1x = a;
  p1y = b;
  p2x = c;
  p2y = d;
}

int main() {

  BBS testBBS (290797);
  cout << testBBS.getNext() << endl;
  cout << testBBS.getNext() << endl;
  cout << testBBS.getNext() << endl;
  cout << testBBS.getNext() << endl;

}
