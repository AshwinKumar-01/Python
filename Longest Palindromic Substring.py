class Solution:
    def longestPalindrome(self, s):
        if s=="":
            return None
        elif s.isspace():
            return None
        elif len(s)==1:
            return s
        else:
            l=0
            tmp=""
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    if(s[i:j]==(s[i:j])[::-1]):
                        if(l<len(s[i:j])):   
                            l=len(s[i:j])
                            tmp=s[i:j]
                    
        return tmp
