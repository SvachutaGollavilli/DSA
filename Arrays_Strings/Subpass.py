"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false"""


class Solution():
    def isSubsequence(self, s, t):
        n1 = len(s)
        n2 = len(t)

        if s == "" or s == t:
            return True
        
        if n1 > n2:
            return False
        
        i = j = 0

        while i < n1 and j <= n2:
            if j == n2 or s[i] != t[j]:
                if j == n2:
                    return False
                
                else:
                    j += 1

            else:
                i += 1
                j += 1

        return True