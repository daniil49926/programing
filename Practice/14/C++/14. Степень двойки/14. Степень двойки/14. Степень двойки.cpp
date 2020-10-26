
#include <iostream>

int main()
{
    setlocale(LC_ALL, "ru");
    int n;
    std::cout << "Введите число" << std::endl; std::cin >> n;
    int rez = 0;
    int multiplicand = 1;
    if (n >= 0) {
        while (multiplicand <= n) {
            multiplicand *= 2;
            rez += 1;
        }
        std::cout << rez << std::endl;
    }
    else
    {
        std::cout << "Введите положительное число." << std::endl;
    }
}