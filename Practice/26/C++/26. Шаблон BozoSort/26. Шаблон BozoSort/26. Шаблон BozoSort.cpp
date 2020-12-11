#include <iostream>
#include <clocale>
#include <vector>
#include <ctime>

using namespace std;

enum Order { up, down };

bool check(vector<int>& a, Order order) {
	switch (order) {
	case up:
		for (int i = 0; i < a.size() - 1; i++) {
			if (a[i] > a[i + 1]) {
				return false;
				break;
			}
		}
		break;
	case down:
		for (int i = 0; i < a.size() - 1; i++) {
			if (a[i] < a[i + 1]) {
				return false;
				break;
			}
		}
		break;
	}

	return true;
}
bool check(int a, int b, int c, Order order) {
	switch (order) {
	case up:
		if (b > c || a > b || a > c) return false;
		break;
	case down:
		if (b < c || a < b || a < c) return false;
		break;
	}
	return true;
}
template<typename T>
std::vector<T> BozoSort(vector<int>& a, Order order = up) {
	bool sorted = check(a, order);
	while (!sorted) {
		int index1 = rand() % a.size();
		int index2 = rand() % a.size();

		int temp = a[index2];
		a[index2] = a[index1];
		a[index1] = temp;

		sorted = check(a, order);

	}
}
template<typename T>
std::vector<T> BozoSort(int& x, int& y, int& z, Order order = up) {
	bool sorted = check(x, y, z, order);
	int temp;
	while (!sorted) {
		int index = rand() % 3;

		switch (index) {
		case 0:
			temp = x;
			x = y;
			y = temp;
			break;
		case 1:
			temp = x;
			x = z;
			z = temp;
			break;
		case 2:
			temp = z;
			z = y;
			y = temp;
			break;
		}
		sorted = check(x, y, z, order);
	}
}

void print(vector<int> a) {
	for (int i = 0; i < a.size(); i++) cout << a[i] << " ";
	cout << endl << endl;
}


void print(int a, int b, int c) {
	cout << a << " " << b << " " << c << endl << endl;
}

int main() {
	setlocale(LC_ALL, "russian");
	srand(time(0));
	int n;
	cin >> n;
	int* a = new int[n];

	for (int i = 0; i < n; i++) cin >> a[i];

	vector<int> b;
	for (int i = 0; i < n; i++) {
		b.push_back(a[i]);
	}

}									//
														//    Шаблон в работе
														//
													//
														//
	