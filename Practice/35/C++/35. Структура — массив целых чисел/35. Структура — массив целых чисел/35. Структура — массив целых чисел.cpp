#include <iostream>

struct IntArray {
    int* data;
    int size;
};

void create(IntArray& arr, const int len){
    arr.data = new int[len];
    arr.size = len;
}

void create(IntArray* arr, const int size){
    create(*arr, size);
}

int get(IntArray& arr, const int index){
    return arr.data[index];
}

int get(IntArray* arr, const int index){
    return get(*arr, index);
}

void set(IntArray& arr, const int index, const int value){
    arr.data[index] = value;
}

void set(IntArray* arr, const int index, const int value){
    set(*arr, index, value);
}

void print(IntArray& arr){
    std::cout << '[';
    for (int i = 0; i < arr.size; i++){
        std::cout << arr.data[i];
        if (i < arr.size - 1){
            std::cout << ", ";
        }
    }
    std::cout << ']' << std::endl;
}

void print(IntArray* arr){
    print(*arr);
}

void resize(IntArray& arr, const int newSize){
    if (newSize > arr.size){
        int* newArr = new int[newSize];
        memcpy(newArr, arr.data, sizeof(int) * arr.size);
        for (int i = arr.size; i < newSize; ++i){
            newArr[i] = 0;
        }
        delete[] arr.data;
        arr.data = newArr;
        arr.size = newSize;
        return;
    }
    int* newArr = new int[newSize];
    memcpy(newArr, arr.data, sizeof(int) * newSize);
    delete[] arr.data;
    arr.data = newArr;
    arr.size = newSize;
}

void resize(IntArray* arr, const int newSize){
    resize(*arr, newSize);
}

void destroy(IntArray& arr){
    delete[] arr.data;
    arr.data = nullptr;
    arr.size = 0;
}

void destroy(IntArray* arr){
    destroy(*arr);
}

int main(){
    int len = 30;
    IntArray arr;
    create(arr, len);
    for (int i = 0; i < len; i++){
        set(arr, i, i + 1);
    }
    print(arr);
    resize(arr, 50);
    print(arr);
    resize(arr, 10);
    print(arr);
    destroy(arr);
}