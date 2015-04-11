def add(*args):
	result = 0
	for num in args:
		result += num
	return result

def mul(*args):
	result = 1
	for num in args:
		result *= num
	return result

def div(*args):
	result = 1
	for num in args:
		result = num / result
	return result

if __name__ == '__main__':
	print add(1, 2, 3)
	print mul(1, 2, 3)
	print div(1, 2, 3)