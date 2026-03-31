"""
Given a string text, you want to use the characters of text 
to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. 
Return the maximum number of instances that can be formed.

 

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""



class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic = {"b": 0, "a":0,"l":0,"o":0,"n":0}

        for char in text:
            if char in dic:
                dic[char] += 1

        for item in dic:
            if dic[item] == 0:
                return 0

        return min(dic["b"], dic["a"], dic["l"]//2, dic["o"]//2, dic["n"])