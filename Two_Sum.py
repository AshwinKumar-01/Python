class Solution:
    def twoSum(self, nums, target):
        length=len(nums)
        for i in range(length):
            for j in range(1,length):
                if nums[i]==nums[j]:
                    if i==j:
                        j+=1
                new=nums[i]+nums[j]
                if new==target:
                    new_lst=[i,j]
                    return new_lst
                    break
