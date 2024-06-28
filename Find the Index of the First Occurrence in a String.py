class Solution:
    def strStr(self, haystack, needle):
        try:
            found=haystack.index(needle)
            return found
        except:
            return -1
