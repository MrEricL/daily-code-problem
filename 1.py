
'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

'''
Explanation: 
Store the complement in a set and check at O(1) time
'''


def fxn(l, k):

	s = set()
	for each in l:
		complement = k-each
		if each in s:
			return set([each, complement])
		else:
			s.add(complement)

	return -1


x = [10, 15, 3, 7]
y = 17
z = set([10, 7])

print(fxn(x, y) == z)
