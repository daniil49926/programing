#include <iostream>
#include <string>
#include <math.h>
int minutes_from_time(std::string);

int main() {
    setlocale(LC_ALL, "ru");
    std::string x1, x2;
    std::cout << "Введите время прихода первого:" << std::endl;
    std::cin >> x1;
    std::cout << "Введите время прихода второго:" << std::endl;
    std::cin >> x2;
    std::cout << std::endl;

    if (abs(minutes_from_time(x1) - minutes_from_time(x2)) < 15 &&
            abs(minutes_from_time(x1) - minutes_from_time(x2)) > 1425 &&
                2359 <= minutes_from_time(x1) >= 0 &&
                    2359 <= minutes_from_time(x2) >= 0)
                {
                    std::cout << "Встреча состоится" << std::endl;
                }
    else if (2359 >= minutes_from_time(x1) <= 0 or
                2359 >= minutes_from_time(x2) <= 0)
               {
                    std::cout << "Ошибка ввода" << std::endl;
               }
        else {
            std::cout << "Встреча не состоится" << std::endl;
             }
    }

int minutes_from_time(std::string time)
{
    size_t a;

    double hours = stoi(time, &a);
    double minutes = stoi(time.substr(a + 1));
    return (hours * 60 + minutes);
}
