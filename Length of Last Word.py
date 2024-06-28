class Solution:
    def lengthOfLastWord(self, s):
        splitted=s.split(" ")
        new=[]
        for i in splitted:
            if len(i)>=1:
                new.append(i)
        return len(new[-1])
