import itertools

class Solution:
    def getPermutation(n: int, k: int) -> str:
        perms = list(itertools.permutations(range(1, n + 1)))
        numbers_string = ''.join(map(str, perms[k - 1])) # This converts each number in the tuple to a string, and then join concatenates these strings into a single string
        return numbers_string

n = 3
k = 3
print(Solution.getPermutation(n, k))