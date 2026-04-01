"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution():
    def long_sub_sequence(self, strs):
        m = len(min(strs, key = len))

        prefix = []

        i = 0
        prefix = []
        while i < m and "" not in strs:
            element = strs[0][i]
            for j, string in enumerate(strs):
                if string[j] == element:
                    if i == (len(strs) - 1):
                        prefix.append(element)
                    continue
                else: 
                    return "".join(prefix)
                
            i += 1

        return "".join(prefix)