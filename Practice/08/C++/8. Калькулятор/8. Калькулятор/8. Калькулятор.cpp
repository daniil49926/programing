#include <iostream>
using namespace std;
int main()
{
	double a, b;
	char oper;
	setlocale(LC_ALL, "Russian");
	cout << "Доступные символы: " "\n" "1 2 3 4 5 6 7 8 9 0""\n" "+ - * /"<<endl;
	cin >> a >> oper >> b;
		if (oper == '*') {
			cout << a * b << endl;
		}
		if (oper == '-') {
			cout << a - b << endl;
		}
		if (oper == '+') {
			cout << a + b << endl;
		}
		if (oper == '/') {
			if (b == 0) {
				cout << "Ошибка" << endl;
				return 0;
			}
			cout << a / b << endl;
		}
	}
	

