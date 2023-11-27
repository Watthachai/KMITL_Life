#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //convert 2 decimal to binary
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    int binary[6];
    int i = 0;
    while (num > 0)
    {
        binary[i] = num % 2;
        num = num / 2;
        i++;
    }
    printf("Binary number is: ");
    for (int j = i - 1; j >= 0; j--)
    {
        printf("%d", binary[j]);
    }
    return 0;
}