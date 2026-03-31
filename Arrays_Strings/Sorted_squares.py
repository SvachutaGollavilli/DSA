"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""



class solution():
    def sorted_squares(self, arr):
        n = len(arr)
        for i in range(n):
            arr[i] = arr[i]**2


        arr = [(i * (-1)) for i in arr]
        l = 0
        r = n-1
        result = [0] * n
        i = 0
        while l < r:
            if arr[l] <= arr[r]:
                result[i] = arr[l]
                l += 1
            else: 
                result[i] = arr[r]
                r -= 1
            i += 1

        result = [(i * (-1)) for i in result]

        return result   




# Clean version

class sorted_1():
    def sorted_squares(self, arr):
        n = len(arr)
        l = 0
        r = n - 1
        i = n - 1
        result = []

        while l < r:
            if abs(arr[l]) >= abs(arr[r]):
                result[i] = arr[l] * arr[l]
                l += 1
            else:
                result[i] = arr[r] * arr[r]
                r -= 1

            i -= 1

        return result


