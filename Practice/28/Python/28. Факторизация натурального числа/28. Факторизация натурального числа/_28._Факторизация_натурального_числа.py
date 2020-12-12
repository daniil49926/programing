
def sum(x, y):
	for key, value in y.items():
		if key in x:
			x[key] += value
		else:
			x[key] = value
	return x

def fact(n):
	for i in range(2, n):
		if (n % i == 0):
			return sum(fact(i), fact(n // i))
	return {
		n:1
		} 

def factor(n: int) -> None:
	temp = fact(n)
	for i in range(len(temp.items())):
		value = list(temp.values())[i]
		key = list(temp.keys())[i]
		print(key, end='');
		if (value > 1):
			print('^', value, sep='', end='')
		if i+1 < len(temp.items()): print('*', end='')
	

x = int(input())
factor(x)
print ('\n')
