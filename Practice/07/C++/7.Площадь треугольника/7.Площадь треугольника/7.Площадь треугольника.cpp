#include <iostream>
#include <cmath>
#include <iomanip>

int main()
{
    double a, b, c, p, S;
    double x1, y1, x2, y2, x3, y3;    //координаты
    setlocale(LC_ALL, "Russian");
    std::cout << "Выберите:" << "\n" << "1)Найти S через длины сторон." << "\n" << "2)Найти S через координаты вершин." << std::endl;
    int choise;
    std::cin >> choise;
    if (choise == 1) {
        std::cout << "a=";
        std::cin >> a;
        std::cout << "b=";
        std::cin >> b;
        std::cout << "c=";
        std::cin >> c;
        p = (a + b + c) / 2;
        S = sqrt(p * (p - a) * (p - b) * (p - c));

        if (S == 0) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (a > (b + c)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (b > (a + c)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (c > (b + a)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else {
            std::cout << "S=" << S << std::endl;
        }
        return 0;
    }
    else if (choise == 2) {
        double S = 0;
        int n = 3;
        std::cout << "A[x, y]" << std::endl;
        std::cin >> x1 >> y1;
        std::cout << "B[x, y]" << std::endl;
        std::cin >> x2 >> y2;
        std::cout << "C[x, y]" << std::endl;
        std::cin >> x3 >> y3;
        a = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
        b = sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1));
        c = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
        p = (a + b + c) / 2;
        S = sqrt(p * (p - a) * (p - b) * (p - c));

        if (S == 0) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (a > (b + c)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (b > (a + c)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else if (c > (b + a)) {
            std::cout << "Такого треугольника не существует" << std::endl;
        }
        else {
            std::cout << "S=" << S << std::endl;
        }
        return 0;
    }
}
