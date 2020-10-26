#include <iostream>

int main()
{
        int l1, l2, r1, r2, S;
        setlocale(LC_ALL, "Ru");
        std::cout << "Введите целые числа через пробел \n S l1 l2 r1 r2" << std::endl;
        std::cin >> S >> l1 >> l2 >> r1 >> r2;
        if (l1 + r2 >= S) {
            r2 = std::max(S - l1, l2);
        }
        else {
            l1 = std::min(S - r2, r1);
        }
        if (l1 + r2 == S) {
            std::cout << l1 << " " << r2 << std::endl;
        }
        else {
            std::cout << -1 << std::endl;
        }
    

}