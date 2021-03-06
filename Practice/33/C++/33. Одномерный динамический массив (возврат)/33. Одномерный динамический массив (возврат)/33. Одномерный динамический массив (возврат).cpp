#include <iostream>

void sort_arr(int* array, int len){
    for (int i = 1; i < len; i++){
        int temp = array[i];
        int value = i - 1;
        while (value >= 0 && array[value] > temp){
            array[value + 1] = array[value];
            array[value] = temp;
            value--;
        }
    }
}

int* create_arr(int len, int start = 0, int step = 0) {
    int* array = new int[len];
    int i = 0;
    for (i; i < len;) {
        array[i] = start;
        start += step;
        i++;
    }
    return array;
}

int* print(int* array, int size){
    std::cout << '[';
    for (int i = 0; i < size; i++){
        std::cout << array[i];
        if (i < size - 1){
            std::cout << ", ";
        }
    }
    std::cout << ']' << std::endl;
    return array;
}

void main(){
    setlocale(LC_ALL, "ru");
    int length_arr;
    int start_point;
    int step;

    std::cout << "Введите длину: ";
    std::cin >> length_arr;
    std::cout << "Введите начальную точку: ";
    std::cin >> start_point;
    std::cout << "Введите шаг: ";
    std::cin >> step;

    int* array = create_arr(length_arr, start_point, step);
    sort_arr(array, length_arr);
    print(array, length_arr);
    delete[] array;
}