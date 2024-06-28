class Solution:
    def myAtoi(self, s):
        string=s.strip()
        l=[]
        s=0
        if len(string)>1:
            if string[0]==".":
                return s
            elif (string[0]=="+" or string[0]=="-") and (string[1]=="-" or string[1]=="+"):
                return s
        elif len(string)==1:
            if string.isdigit():
                return int(string)
            else:
                return s
        elif len(string)==0:
            return s
            
        
        for k in string:
            if k.isdigit():
                l.append(k)
            elif k==".":
                break
        if len(l)==1:
            output=int(l[0])
        else:
            output=int(''.join(l))
        if string[0]=='-':
            output*=-1
        if output>((2**31)-1):
            output=((2**31)-1)
        elif output < ((-2**31)):
            output=((-2**31))
        elif len(l)==0 or ((string[0].isalpha())):
            output=0
        return output
