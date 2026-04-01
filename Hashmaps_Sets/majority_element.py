"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# Solution 1. Time : O(n), space: O(n).
from collections import defaultdict

class solution():
    def majority_element(self, nums):
        dic = defaultdict()
        for num in nums:
            if num not in dic:
                dic[num] = 1

            else:
                dic[num] += 1

        max_value = -1
        answer = -1

        for key, value in dic:
            if value > max_value:
                max_value = value
                answer = key
        
        return answer
    

# Solution 2. Time: O(n), space: O(1)
# This is a bit intuitive that the majority element count is always greater than n/2

class sol2():
    def majority(self, nums):
        count = res = 0

        for num in nums:
            if count == 0:
                res = num

            count += (1 if res == num else -1)


        return res