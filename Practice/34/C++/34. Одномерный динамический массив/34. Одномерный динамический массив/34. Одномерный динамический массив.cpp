#include <iostream>


void sort_arr(int* arr, int len) {
    for (int i = 1; i < len; i++) {
        int temp = arr[i];
        int value = i - 1;
        while (value >= 0 && arr[value] > temp) {
            arr[value + 1] = arr[value];
            arr[value] = temp;
            value--;
        }
    }
}

int* create_arr(int len, int start = 0, int step = 0){
    int* arr = new int[len];
    for (int i = 0; i < len; i++){
        arr[i] = start;
        start += step;
    }
    return arr;
}

void create_arr(int** arr, int len, int start, int step){ *arr = create_arr(len, start, step); }

void del_arr(int** arr){
    if (arr == nullptr){
        return;
    }
    delete[] * arr;
    *arr = nullptr;
}

int* print(int* arr, int size){
    std::cout << '[';
    for (int i = 0; i < size; i++){
        std::cout << arr[i];
        if (i < size - 1){
            std::cout << ", ";
        }
    }
    std::cout << ']' << std::endl;
    return arr;
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
    int* arr;
    create_arr(&arr, length_arr, start_point, step);
    sort_arr(arr, length_arr);
    print(arr, length_arr);
    del_arr(&arr);
}