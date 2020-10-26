
#include <iostream>
#include<math.h>

int main()
{
    double a;
    int x;
    int i; i = 1;
    double z;
    setlocale(LC_ALL, "ru");
    std::cout << "Введите число возводимое в степень" << std::endl; std::cin >> a;
    std::cout << "Введите степень" << std::endl; std::cin >> x;
    z = a;
    while (i < abs(x)) {
        a = a * z;
        i++;
    }
    if (x > 0) {
        std::cout << "Результат = " << a << std::endl;
        return 0;
    }
    else if (x < 0) {
        std::cout << "Результат = " << 1/a << std::endl;
        return 0;
    }
    else if (x == 0) {
        std::cout << "Результат = " << 1 << std::endl;
        return 0;
    }
}

