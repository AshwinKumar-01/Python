class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        elif s.isspace():
            return 1
        elif len(s)==1:
            return len(s)
        else:
            n = len(s) 
            # Result 
            res = 0 
            for i in range(n):
                # Note : Default values in  
                # visited are false 
                visited = [0] * 256
                for j in range(i, n): 
                    # If current character is visited 
                    # Break the loop 
                    if (visited[ord(s[j])] == True): 
                        break
                    # Else update the result if 
                    # this window is larger, and mark 
                    # current character as visited. 
                    else: 
                        res = max(res, j - i + 1) 
                        visited[ord(s[j])] = True
                    # Remove the first character of previous 
                    # window 
                #visited[ord(s[i])] = False
        return res
