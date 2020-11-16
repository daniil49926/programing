#ifndef HED
#include "fact.h"
#define HED


int h(int k, int i)
{
	int rez;
	rez = fact(i) / (fact(k) * fact(i - k));
	return rez;
}


#endif