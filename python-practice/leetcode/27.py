class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                nums.append(-1)
            elif nums[i] == -1:
                break
            else:
                i += 1
        return i
    
print(Solution.removeElement([0,1,2,2,3,0,4,2], 2))

'''
Scanning through the entire array, check if an element of the array is equal
to the given 'val'. If it is, remove it from the list and then append -1 to
the end of the list (in order to maintain the same length of the list).
If we reach -1, we have found all the occurances of the desired element and
removed it.
'''