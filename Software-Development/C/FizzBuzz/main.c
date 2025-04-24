#include <stdio.h>
#include <string.h>

int main (void) {

    unsigned char again = 'y';

    while (again == 'y')
    {

        // Game
	int input;

        printf("Input a number:\n");
        scanf("%i", &input);

        if ((input % 5 == 0) && (input % 3 == 0)) {
            printf("FizzBuzz\n");
        }
        else if (input % 3 == 0) {
            printf("Buzz\n");
        } else {
            printf("Fizz\n");
        }

        // Loop controller

        printf("Play again? [y/n]\n");

        scanf(" %c", &again);
    }

    return 1;
}
