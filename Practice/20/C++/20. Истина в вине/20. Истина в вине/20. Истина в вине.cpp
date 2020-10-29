#include <iostream>

int main()
{
	setlocale(LC_ALL, "ru");
	int money;//деньги
	int quantity;//кол-во нап.
	std::string name_of_the_alkashka;//название алк
	int price;//цена
	int size;//объем
	int pricelit;//цена л
	bool flag = true;
	int remainder;//сдача
	int can_buy;//
	int sumV = 0;//может купить л
	int sizen;
	std::string chosen_name_of_the_alkashka;
	int n_alkaski;
	std::cout << "Сколько у вас денег и сколько напитков вы видите в магазине?" << std::endl;
	std::cin >> money >> quantity;
	for (int i = 0; i < quantity; ++i) {
		std::cout << "Напиток,сколько стоит,сколько литров в бутылке?" << std::endl;
		std::cin >> name_of_the_alkashka >> price >> size;
		pricelit = price / size; n_alkaski = money / pricelit;
		if (n_alkaski >= 1 && n_alkaski > sumV) {
			chosen_name_of_the_alkashka = name_of_the_alkashka;
			remainder = money - (n_alkaski * pricelit);
			sizen = size;
			sumV = n_alkaski;
			flag = false;
		}
	}
	if (flag == true) std::cout << "-1" << std::endl;
	else if (flag == false) {
		std::cout << "Чтобы отлично отдохнуть,вам нужно:" << std::endl;
		std::cout << chosen_name_of_the_alkashka << " " << sizen <<" л" <<std::endl;
		std::cout << sumV <<"-всего л" <<std::endl;
		std::cout << remainder << "-сдача" << std::endl;
	}
}