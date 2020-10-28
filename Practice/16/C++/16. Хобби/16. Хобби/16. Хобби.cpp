#include <iostream>
#include <cstring>

int main()
{
    setlocale(LC_ALL, "ru");
    int quantity;
    int i = 0;
    int a = 1;
    std::string ticket;
    std::cout << "Введите количество билетов: ";
    std::cin >> quantity;
    std::cout << "Введите номера билетов(через пробел): ";
    for (int i = 0; i < quantity; i++)
    {
        std::cin >> ticket;
        if (ticket.length() != 9) {
            continue;
        }
        else {
            if (ticket[0] == 'a' && ticket[4] == '5'
                && ticket[5] == '5' && ticket[6] == '6'
                && ticket[7] == '6' && ticket[8] == '1')
            {
                std::cout << ticket << std::endl;
                a = 0;
                continue;
            }
        }
    }
    if (a == 1) {
        std::cout << -1 << std::endl;
    }
}