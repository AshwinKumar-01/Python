class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        while nums1 or nums2:
            new_lst=nums1+nums2
            #print(new_lst)
            new_lst=sorted(new_lst)
            #print(new_lst)
            med=len(new_lst)//2
            s=(new_lst[med]+new_lst[~med])/2
            return s
