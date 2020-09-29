
#include <iostream>
using namespace std;

int main()
{
    double a, b, c, x;
    setlocale(LC_ALL, "Russian");
    cout << "Введите данные для уровнения типа ax^2+bx+c=0" << endl << "a=";
    cin >> a;
    cout << "b=";
    cin >> b;
    cout << "c=";
    cin >> c;
    double D = b * b - 4 * a * c;
    if (D > 0) {
        x = (-1 * b + sqrt(D)) / (2 * a);
        cout << "x1=" << x << endl;
        x = (-1 * b - sqrt(D)) / (2 * a);
        cout << "x2=" << x << endl;
    }
    if (D == 0) {
        x = (-1 * b + sqrt(D)) / (2 * a);
        cout << "x=" << x << endl;
    }
    else {
        cout << "уравнение не имеет корней" << endl;
    }
    
}
