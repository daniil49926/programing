#include<iostream>

int main()
{
	int numbers[37]{ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36 };
	int red[18]{ 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 }; 
	int black[18]{ 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 };
	int last_game = 12;
	int drop[37]; int dropmax [37]{}; int dropmaxbigger = 0;
	int inp;
	int sumblack = 0; int sumred = 0;
	int i = 0;
	int flag = 1;
	while (flag == 1){
		std::cin >> inp;
		if (inp < 0 || inp > 36){
			flag=0;
			break;
		}
		else{
			for (int i = 0; i < 37; i++){
				if (numbers[i] == inp) drop[i] = i;
			}
		}
		dropmax[inp] = dropmax[inp] + 1;
		for (int i = 0; i < 37; i++){
			if (dropmax[i] > dropmaxbigger)
				dropmaxbigger = dropmax[i];
		}
		for (int i = 0; i < 37; i++){
			if (dropmax[i] == dropmaxbigger)
				std::cout << numbers[i] << " ";
		}
		std::cout << std::endl;
		for (int i = 0; i < 19; i++){
			if (inp == black[i]) sumblack = sumblack + 1;
			else if (inp == red[i]) sumred = sumred + 1;
		}
		for (int i = 0; i < 37; i++){
			if (drop[i] == 0 || i - drop[i] >= last_game)
				std::cout << numbers[i] << " ";
		}
		std::cout << '\n';
		std::cout << sumred << " " << sumblack << "\n\n\n";
		i++;
	}
}

