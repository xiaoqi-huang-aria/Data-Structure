int main()
{
    int i, sum = 0;
    int n[10];

    for ( i = 0; i < 10; i++ ) {
        n[ i ] = i + 100;
    }

    for ( i = 1; i <= LAST; i++ ) {
        sum += i;
    }
    printf("sum = %d\n", sum);

    return 0;
}