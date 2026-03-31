"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# Solution 1 is good for fixed constraint in charecters (a-z)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False


        Char_value = [0] * 26
        for i in range(len(s)):
            Char_value[(ord(s[i])-ord('a'))] += 1
            Char_value[(ord(t[i])-ord('a'))] -= 1

        for value in Char_value:
            if value != 0:
                return False

        return True
    

#solution 2 is flexible for more charecter variations
class solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1

            else:
                dic[letter] += 1

        for letter in t:
            if letter not in dic:
                return False

            elif dic[letter] == 0:
                return False

            else:
                dic[letter] -= 1

        for letter in dic:
            if dic[letter] != 0: 
                return False

        return True