
#include <iostream>

int main()
{
    int x,y,x1,y1;
	char oper;
    int h1[23];
    int h2[23];
    int m1[59];
    int m2[59];
	setlocale(LC_ALL, "Russian");
    std::cout << "Введите время прихода первого" << std::endl;
	while (true) {
		std::cin >> x >> oper >> y;
		if (std::cin.good()) {
			std::cin.ignore(10, '\n');
			break;
		}
		std::cin.clear();
		std::cout << "Неправильный ввод" << std::endl;
		std::cin.ignore(10, '\n');
	}
	if (h1[23] == x, oper == ':', m1[59] == y) {
		std::cout << "Введите время прихода второго" << std::endl;
		while (true) {
			std::cin >> x1 >> oper >> y1;
			if (std::cin.good()) {
				std::cin.ignore(10, '\n');
				break;
			}
			std::cin.clear();
			std::cout << "Неправильный ввод" << std::endl;
			std::cin.ignore(10, '\n');
		}
		if (h1[23] == x1, oper == ':', m1[59] == y1) {
			if (y <= y1) {
				std::cout << "встреча состоиться";
			}
			else {
				std::cout << "встреча не состоиться";
			}
		}
	}

}

