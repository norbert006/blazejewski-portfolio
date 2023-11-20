class Solution:
    def lengthOfLastWord(s: str) -> int:
        last_word = s.split()[-1]
        count = 0
        for char in last_word:
            count += 1
        return count
    
print(Solution.lengthOfLastWord("Hello World"))