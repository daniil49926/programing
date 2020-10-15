#include<cmath>
#include <iostream>
using namespace std;

int main()
{
    double g = 9.8, z, v, t;
    setlocale(LC_ALL, "Russian");
    cout << "Введите параметры для формулы x(t)=x0+v0t-at^2/2 " << endl << "X0"<<endl;
    cin >> z;
    cout << "V0" << endl;
    cin >> v;
    cout << "t"<<endl;
    cin >> t;
    double x = z + v * t - (g * t * t)/2;
    double S = x - z;
    cout <<"Расстояние = "<< abs(S) << endl;
}
// Для переменных данной формулы лучше использовать переменные типа double,тк в таких переменных может храниться дробное число. 