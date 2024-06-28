class Solution:
    def searchInsert(self, nums, target):
        try:
            res=nums.index(target)
            return res
        except:
            for i in range(len(nums)):
                if nums[i]>target or nums[i]==target:
                    return i
            else:
                return len(nums)
