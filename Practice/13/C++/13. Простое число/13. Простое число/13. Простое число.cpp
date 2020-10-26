
#include <iostream>
#include <math.h>

int main()
{
    int n;
    bool flag = true;
    setlocale(LC_ALL, "ru");
    std::cout << "Введите число:" << std::endl; std::cin >> n;
    if (n >= 2) {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                flag = false;
                break;
            }
        }

        if (flag == true) {
            std::cout << "Простое" << std::endl;
        }
        else {
            std::cout << "Сложное" << std::endl;
        }
    }
    else if(n <= 1) {
        std::cout << "Число должно быть больше 1" << std::endl;
    }
}