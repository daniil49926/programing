
#include <iostream>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int y = b, z = a;
    cout << y <<" "<< z << endl;

    cin >> a >> b;
    a = a + b;
    b = b - a;
    b = -b;
    a = a - b;
    cout << a << " " << b << endl;
}

