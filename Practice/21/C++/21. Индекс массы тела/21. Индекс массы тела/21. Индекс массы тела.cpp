
#include<iostream>

double BMI(double weight, double height)
{
	return weight / pow(height, 2);
}
void printBMI(double BMI)
{
	if (BMI < 18.5)
		std::cout << "Underweight"; if (BMI >= 18.5 && BMI < 25.0) std::cout << "Normal";
	if (BMI >= 25.0 && BMI < 30) std::cout << "Overweight"; if (BMI >= 30.0) std::cout << "Obesity";
}

int main()
{
	std::cout << "weight && height: ";
	double weight,height;
	std::cin >> weight >> height;
	height /= 100;
	printBMI(BMI(weight, height));

}