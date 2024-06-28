class Solution:
    def plusOne(self, digits):
        new=[]
        res=""
        for i in digits:
            res+=str(i)
        res=str(int(res)+1)
        for i in res:
            new.append(int(i))
        return list(new)
