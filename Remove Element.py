class Solution:
    def removeElement(self, nums, val):
        i=0
        while i < len(nums):
            print(len(nums))
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return nums
