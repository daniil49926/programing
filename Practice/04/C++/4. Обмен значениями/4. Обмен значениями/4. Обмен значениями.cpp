
#include <iostream>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    swap(a, b);
    cout << a <<" "<< b << endl;

    cin >> a >> b;
    a = a + b;
    b = b - a;
    b = -b;
    a = a - b;
    cout << a << " " << b << endl;
}

