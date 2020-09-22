
#include <iostream>

using namespace std;

int main()
{
	int x, y;
	setlocale(LC_ALL, "Russian");
	cout << "Введите числа" << endl;
	cin >> x >> y;
	cout << x + y << " " << x - y << " " << x * y << " " << x / y << endl;

	double z, c;
	setlocale(LC_ALL, "Russian");
	cout << "Введите числа" << endl;
	cin >> z >> c;
	cout << z + c << " " << z - c << " " << z * c << " " << z / c << endl;

	double v;
	int b;
	setlocale(LC_ALL, "Russian");
	cout << "Введите числа" << endl;
	cin >> v >> b;
	cout << v + b << " " << v - b << " " << v * b << " " << v / b << endl;

	int n;
	double m;
	setlocale(LC_ALL, "Russian");
	cout << "Введите числа" << endl;
	cin >> n >> m;
	cout << n + m << " " << n - m << " " << n * m << " " << n / m << endl;

}

