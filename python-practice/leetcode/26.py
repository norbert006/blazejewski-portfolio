class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        l_pointer = 1
        for r_pointer in range(1, len(nums)):
            if nums[r_pointer] != nums[r_pointer - 1]:
                nums[l_pointer] = nums[r_pointer]
                l_pointer += 1
        return l_pointer

print(Solution.removeDuplicates([1,1,2,3,4]))


'''
Left pointer (l_pointer) starts with the 2nd value in the array because the first value
will always be unique (a single number cannot have a duplicate because there is only one).
The right pointer scans through the entire array to find the first occurance of a unique
value.
The left pointer is updated with the newly found unique value and its index is incremented 
after each such find.

'''