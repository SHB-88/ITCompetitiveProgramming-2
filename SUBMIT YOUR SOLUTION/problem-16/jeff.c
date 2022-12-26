#include <stdio.h>;

    int main()
{
    int number, reversed = 0, tmp;
    printf("Enter any number = ");
    scanf("%d", &number);
    tmp = (number < 0)?(-1 * number): number;
    reversed = RD(tmp);
    reversed = (number < 0)? (-1 * reversed): reversed;
    printf("Reverse of no. is %d", reversed);
    return 0;
}
    int RD(int num)
{
    static int rev_num = 0;
    static int base_pos = 1;
    if(num > 0)
    {
        RD(num/10);
        rev_num += (num%10)*base_pos;
        base_pos *= 10;
    }
    return rev_num;
}
