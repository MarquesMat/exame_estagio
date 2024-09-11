// Exercício 3

#include <stdio.h>

int main(void) {
    int ind = 12, sum = 0, k = 1;
    while(k<ind) {
        k++;
        sum += k;
    }
    printf("Total da soma: %d", sum);
}