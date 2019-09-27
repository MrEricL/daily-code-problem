'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

https://leetcode.com/problems/first-missing-positive/
'''


'''
Explanation: 
Swap until everything is in the correct index corresponding
Iterate checking index with value where index + 1 = value
'''

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        val = nums[i]

        # keep move everything into it's correct index
        # i = 1         nums = [-1 4 3 1]
        # swap(4,1)     nums = [-1 1 3 4]
        # swap(1,-1)    nums = [1 -1 3 4]
        # 1 is now in the right index location
        # terminates if 0 > x  or x > n

        while val > 0 and val <= len(nums) and nums[val-1] != val:
            nums[i], nums[val-1] = nums[val-1], nums[i]
            val = nums[i]

    for i in range(len(nums)):
        if i+1!= nums[i]:
            return i+1

    return len(nums)+1 # edge case for len = 0


        


print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))
print(firstMissingPositive([7,0,9,1,2]))