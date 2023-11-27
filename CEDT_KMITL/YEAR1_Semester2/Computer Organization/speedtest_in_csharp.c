#include <stdio.h>
#include <time.h>

// Assembly function to add two numbers
extern int speedtest_in_assembly(int a, int b);

int main() {
    int num1 = 0;
    int num2 = 0;
    int result;
    int i;
    double time_spent_c, time_spent_assembly;

    // Test speed in C
    time_t begin_c = clock();
    for(i = 0; i < 100000000; i++) {
        result = num1 + num2;
    }
    time_t end_c = clock();
    time_spent_c = (double)(end_c - begin_c) / CLOCKS_PER_SEC;

    // Test speed in assembly
    time_t begin_assembly = clock();
    for(i = 0; i < 100000000; i++) {
        result = speedtest_in_assembly(num1, num2);
    }
    time_t end_assembly = clock();
    time_spent_assembly = (double)(end_assembly - begin_assembly) / CLOCKS_PER_SEC;

    printf("Time Speed C: %f seconds\n", time_spent_c);
    printf("Time Speed Assembly: %f seconds\n", time_spent_assembly);

    return 0;
}
