class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        strs.sort()
        size=len(strs)
        end=min(len(strs[0]), len(strs[size-1]))
        print(end)
        i=0
        while (i<end and strs[0][i]==strs[size-1][i]):
            i+=1
        pre=strs[0][:i]
        return pre
