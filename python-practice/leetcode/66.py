class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        digits = digits[::-1] # Reverse the list.
        one, i = 1, 0 # One is the value 1 that is used to carry over (like in standard addition), i is index.

        while one: # While one is still 1.
            if i < len(digits): # While the index is within valid range.
                if digits[i] == 9: # If the digit is 9, turn it into 0 (then the 1 can get carried over to the next digit).
                    digits[i] == 0
                else: # If the digit is not 9, just add 1 to it. This will stop the loop.
                    digits[i] += 1
                    one = 0
            else: # When the index becomes out of range. For example, when we are adding 1 to 999. This also stops the loop.
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1] # Reverse list back to original order.


print(Solution.plusOne([1,2,9]))