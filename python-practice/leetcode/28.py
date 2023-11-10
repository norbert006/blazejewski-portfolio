class Solution:
    def strStr(haystack: str, needle: str) -> int:
        check_stack = []
        first_occurance = 0
        hay_index = 0
        needle_index = 0
        if needle not in haystack:
            return -1
        else:
            while needle_index < len(needle):
                print(check_stack)
                if needle[needle_index] != haystack[hay_index] and not bool(check_stack):
                    hay_index += 1
                    continue
                elif needle[needle_index] == haystack[hay_index] and not bool(check_stack):
                    first_occurance = hay_index
                    check_stack.append(haystack[hay_index])
                    needle_index += 1
                    hay_index += 1
                    continue
                elif needle[needle_index] == haystack[hay_index] and bool(check_stack):
                    check_stack.append(haystack[hay_index])
                    needle_index += 1
                    hay_index += 1
                    continue
                elif needle[needle_index] != haystack[hay_index] and bool(check_stack):
                    check_stack.clear()
                    needle_index = 0
                    hay_index = first_occurance + 1
                    continue
        return first_occurance
    
print(Solution.strStr("mississippi", "issip"))

'''
This solution goes through every value at every index in the needle and compares it to every
value at every index in the haystack. If there is a match, this value is added to the stack.
If the needle is "broken", the stack clears and the index of the haystack is moved back to
the first occurance (+1) where the haystack and needle matched.


Alternative solution:

if needle == "":
    return 0

for i in range(len(haystack) + 1 - len(needle)):
    if haystack[i: i + len(needle)] == needle:
        return i
return -1

'''

                
        