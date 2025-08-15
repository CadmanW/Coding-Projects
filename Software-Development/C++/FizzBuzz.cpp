/*

Concept:
If a number entered is divisible by 3, output FIZZ.
If it's divisible by 5, output BUZZ
If it's divisible by both 3 and 5, output FIZZBUZZ

*/



#include <iostream>

using namespace std;

int main(void) {

    int num{};

    cout << "Enter a number: ";
    cin >> num;

    for (int i = 1; i <= num; i++) {
        string output{};

        if (i % 3 == 0 && i % 5 == 0) {
            output = "FIZZBUZZ";
        }
        else if (i % 3 == 0) {
            output = "FIZZ";
        }
        else if (i % 5 == 0) {
            output = "BUZZ";
        }

        cout << i << ": " << output << endl;
    }

    return 0;
}