#include <iostream>
#include "fact.h"
#include "sin.h"
#include "Header.h"
using namespace std;
int main()
{
	cout << "n"<<"\t"<<"n!\n";
	for (int i = 1; i <= 10; i++) 
	{
		cout << i << "\t" << fact(i) << "\n";
	}
	cout << "\n" << "x"<<"\t"<<"sin(x)" << "\n";
	int k = 5;
	for (double x = 0; x <= 3.141592653589793 / 4; x = (x + 3.141592653589793 / 180))
	{
		cout << x << "\t" << sinx(x,k) << "\n";
	}
	cout << "\n" << "k"<<"\t"<<"C(k, 10)" << "\n";
	for (int k = 1; k <= 10; k++)
	{
		cout << k << "\t" << h(k, 10) << "\n";
	}
}

