def add(numbers =0, *args):
	result = 0
	for num in numbers:
		result += num
	for num in args:
		result += num
	return result

def mul(numbers =0, *args):
	result = 1
	for num in numbers:
		result *= num
	for num in args:
		result *= num
	return result

def div(numbers =0, *args):
	result = 1
	for num in numbers:
		result = num / result
	for num in args:
		result = num / result
	return result

def sub(numbers =0, *args):
	result = 0
	for num in numbers:
		result -= num
	for num in args:
		result -= num
	return result

if __name__ == '__main__':
	numbers = [1, 2, 3, 4]
	print "Sum of: " + str(numbers) + " = " + str(add(numbers, 1, 2))
	print "Product of: " + str(numbers) + " = " + str(mul(numbers))
	print "Division of: " + str(numbers) + " = " + str(div(numbers))
	print "Subtraction of: " + str(numbers) + " = " + str(sub(numbers))