#pragma once

int fact(int n)
{
	int i = 1;
	int rez = 1;
	for ( i ; i <= n; i++)
		rez =rez * i;
	return rez;

}