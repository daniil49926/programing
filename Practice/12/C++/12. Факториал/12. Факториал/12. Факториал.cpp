
#include <iostream>

int main()
{
    setlocale(LC_ALL, "ru");
    int n;
    std::cout << "Введите целое число:" << std::endl; std::cin >> n;
    int rez = 1;
    if (n >= 0) {
        for (int i = 1; i <= n; i++)
        {
            rez *= i;
        }
        std::cout << rez;
    }
    else {
        std::cout << "Введите целое положительное число!" << std::endl;
    }
}

