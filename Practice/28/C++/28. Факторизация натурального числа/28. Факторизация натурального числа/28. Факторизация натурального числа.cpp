#include <iostream>


void factor(int n, int x = 2)
{
    if (n == 1) return;
    if (n % x == 0)
    {
        std::cout << " * " << x;
        factor(n / x, x);
    }
    else
        if (x == 2)
            factor(n, x + 1);
        else
            factor(n, x + 2);
}
int main()
{
    int n;
    std::cin >> n;
    std::cout << n<<" = 1";
    factor(n, 2);
    std::cin.get(); 
    std::cin.get();
    return 0;
}