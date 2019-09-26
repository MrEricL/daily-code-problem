
'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''


def fxn(x):

	ret = [1 for i in range(len(x))]
	rety = [1 for i in range(len(x))]

	p = 1
	for i in range(len(x)):
		ret[i] = p
		p *= x[i]
		#print (p)

	p = 1
	for i in range(len(x)-1, -1, -1):
		rety[i] = ret[i]*p
		p *= x[i]
		#print(p)

	return rety


x = [3, 2, 1]
y = [2, 3, 6]
print(fxn(x) == y)

a = [1, 2, 3, 4, 5]
b = [120, 60, 40, 30, 24]
print(fxn(a) == b)