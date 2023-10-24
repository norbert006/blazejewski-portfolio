class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])): 
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res

print(Solution.longestCommonPrefix(["flower","flow","flight"]))

'''
Lines 5:
Start a loop that iterates over the indices of characters in the first string. 
The loop runs from 0 to the length of the first string (strs[0]), assuming that 
the first string is the shortest or at least as long as the shortest string in the list.

Line 6:
Start another loop that iterates through each string s in the strs list.

Line 7:
Check two conditions:
1. If the current index i is equal to the length of the string s, it means that the current string 
   s is shorter than the prefix found so far, and you return res.
2. If the character at index i in the current string s is not equal to the character at the same 
   index i in the first string (strs[0]), you also return res.
'''