#include <iostream>
#include <fstream>
#include <vector>
std::ostream& operator<< (std::ostream& v, std::vector<int> arr) {
    v << arr.size() << "\t","|"," ";
    for (auto& i : arr) v << &i << " ";
    return v << std::endl;
}

void main() {
    std::vector<int> arr;
    std::ofstream data;
    data.open("data.txt");
    for (int j = 0; j < 64; j++) {
        arr.push_back(rand());
        data << arr;
    }
    for (int j = 0; j < 64; j++) {
        arr.pop_back();
        data << arr;
    }
    for (int j = 0; j < 64; j++){
        arr.push_back(rand());
        data << arr;
    }
    for (int j = 0; j < 64; j++) {
        arr.pop_back();
        data << arr;
    }
}