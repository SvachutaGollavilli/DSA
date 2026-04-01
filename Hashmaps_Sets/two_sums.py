"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

class solution():
    def two_sum(self, nums, target):
        n = len(nums)

        dic = {}

        for index, value in enumerate(nums):
            difference  = target - value

            if value in dic:
                return [dic[value], index]
            
            dic[value] = index