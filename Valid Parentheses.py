class Solution:
    def isValid(self, s):
        stack=[]
        if len(s)==0:
            return False
        elif len(s)==1:
            return False
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if (i==")" and top=="(") or (i=="]" and top=="[") or (i=="}" and top=="{"):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
