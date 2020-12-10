#include<iostream>
#include<cmath>

void main() {
	int n;
	std::cin >> n;
	int *arr = new int [n];

	for (int i = 0; i < n; i++) {
		std::cin >> arr[i];
       
        for (int j = 0; j < 5; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                if (arr[j] < arr[k])
                {
                    int temp = arr[k];
                    arr[k] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        if (i == 0)std::cout << arr[0] << std::endl;
        if (i == 1)std::cout << arr[0] << arr[1] << std::endl;
        if (i == 2)std::cout << arr[0] << arr[1] << arr[2] << std::endl;
        if (i == 3)std::cout << arr[0] << arr[1] << arr[2] << arr[3] << std::endl;
        if (i == 4)std::cout << arr[0] << arr[1] << arr[2] << arr[3] << arr[4] << std::endl;
        if (i > 4) {
                std::cout << arr[i - 4] << arr[i - 3] << arr[i - 2] << arr[i - 1] << arr[i] << std::endl;
            }
        

	}




}