"""You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other,
 append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""


class solutuion():
    def merge_strings(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        i = j = 0
        result = []

        while i < l1 and j < l2:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
            j += 1

        while i < l1:
            result.append(word1[i])
            i += 1

        while j < l2:
            result.append(word2[j])
            j += 1

        return "".join(result)
    



# Better Solution

class solutuion1():
    def merge_strings(self, word1, word2):
        i = 0
        l1 = len(word1)
        l2 = len(word2)
        result = []

        while i < l1 or i < l2:
            if i < l1:
                result.append(word1[i])
            if i < l2:
                result.append(word2[i])
            i += 1

        return "".join(result)

        

