#ifndef SIN_H
#include "fact.h"
#include <math.h>
#define SIN_H

double sinx(double x, double k)
{
    int i = 0;
    double rez = 0;
    for ( i; i < k; i++)
        rez = rez + pow(-1, i) * (pow(x, 2 * i + 1) 
                     / (fact(2 * i + 1)));
    return rez;
}

#endif