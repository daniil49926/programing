#include <iostream>
#include<map>


void factor(int n)
{
    std::map  <int, int> in;
    int x = 2;
    while (n > 1)
    {
        for (int i = 2; i <= n; i++)
        {
            if (!(n % i))
            {
                n /= i;

                in[i] = in.count(i) ? in[i] + 1 : 1;
                break;
            }
        }
    }
    std::cout << "1";
    for (auto now : in)
    {
        if (now.second > 1)
        {
            std::cout << "*" << now.first << "^" << now.second;
        }
        else
        {
            std::cout << "*" << now.first;
        }
    }
}
int main()
{
    int n;
    std::cin >> n;
    factor(n);
}
