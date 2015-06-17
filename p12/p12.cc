#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector<int> primes;

void GenPrimes() {
    primes.push_back(2);
    for (int i = 3; i < 1000000; i+=2) {
        for (auto j : primes) {
            if( i % j == 0) {
                break;
            }
            if( j > sqrt(i) ) {
                primes.push_back(i);
                break;
            }
        }
    }
}

int numDivisors(long input) {
    vector<int> nums;
    long old_input_sqrt = ceil(sqrt(input));
    for(auto p : primes) {
        if(p > old_input_sqrt) {
            if(nums.size() == 0) {
                return 2;
            }
            break;
        }
        int current_num = 0;
        while(input % p == 0) {
            current_num++;
            input /= p;
        }
        if(current_num > 0) {
            nums.push_back(current_num);
        }
    }
    int total = 1;
    for(auto num : nums) {
        total*= (num+1);
    }
    return total;
}

int main() {
    GenPrimes();
    long current = 1;
    long addr = 2;
    while(1) {
        current+=addr;
        addr++;
        if (numDivisors(current) > 500) {
            cout << current << endl;
            break;
        }
    }
}
