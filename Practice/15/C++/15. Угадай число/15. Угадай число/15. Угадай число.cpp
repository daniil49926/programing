#include <iostream>
#include <cstdlib>
#include<ctime>
int main()
{
    setlocale(LC_ALL, "russian");
    srand(time(NULL));
    int number = rand()%101;
    int choice;
    std::cout << "Привествую в игре!" << "Угадай число" << std::endl << "Начнем?\n\"ДА-1\"\n\"НЕТ-любое другое число\"" << std::endl;
    int pick;
    std::cin >> pick;
    again:
    int i=0;
    for (i;pick==1 ;i=i) {
        while (pick == 1 && i < 5)
        {
            std::cout << "Введите число: ";
            std::cin >> choice;
            std::cout << std::endl;

            if (choice < number)
            {
                std::cout << "Загаданное число больше" << std::endl;
            }
            else if (choice > number)
            {
                std::cout << "Загаданное число меньше" << std::endl;
            }
            else if (choice == number)
            {
                pick = 0;
                std::cout << "Поздравляю! Вы угадали\nХотите начать еще?\n\"ДА-1\"\"НЕТ-любое другое число\"" << std::endl;
                std::cin >> pick;
                if (pick == 1) {
                    continue ;
                }
                else {
                    break;
                }
            }
            i++;
        }
        if (i == 5)
        {
            std::cout << "Вы проиграли(( "<<"Загаданное число ="<<number<<"\nХотите начать еще?\n\"ДА-1\"\"НЕТ-любое другое число\"" << std::endl;
            std::cin >> pick;
            if (pick == 1) {
                goto again;
            }
            else {
                break;
            }
        }
    }
}
