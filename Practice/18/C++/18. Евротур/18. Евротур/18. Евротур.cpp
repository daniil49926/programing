#include <iostream>
#include <string>
using namespace std;
int main()
{
    setlocale(LC_ALL, "ru");
    const string ws[] = { "hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen" };
    int chars[26] = {};
    const int i = 'a';
    double probability = 1; double sum = 0;
    cout << "Введите стоп слово:" << endl;
    string stopslovo; 
    getline(cin, stopslovo);
    for (const string& w : ws)
    {
        for (const char& chr : w)
        {
            ++chars[chr - i];
        }
    }
    for (const int& i : chars)
    {
        sum = sum + i;
    }
    for (const char& chr : stopslovo)
    {
        probability = probability * chars[chr - i] / sum;
        if (probability < LDBL_EPSILON)
            break;
    }
    cout << probability << endl;
}
