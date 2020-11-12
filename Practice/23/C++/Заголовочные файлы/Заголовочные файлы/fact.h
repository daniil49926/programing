#pragma once
#include <iostream>
void fact()
{
    int rez = 1;
        for (int i = 1; i <= 10; i++)
        {
            rez *= i;
            std::cout << i<<"\t"<<rez;
        }
        
}