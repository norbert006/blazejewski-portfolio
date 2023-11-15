class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target: # If target value found
                return mid # We only need to return the index of the target value.
            
            if target > nums[mid]: # If the target value is greater than the mid value.
                l = mid + 1
            else: # If the target value is less than the mid value.
                r = mid - 1
        
        return l # Return left pointer

nums = [1,3,5,6]
target = 5
print(Solution.searchInsert(nums, target))

'''
Solved using Binary Search.
'''