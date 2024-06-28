class Solution:
    def letterCombinations(self, digits):
        result = [""]
                if not digits: return []
                dicts = {
                    "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz",
                }
                for i in digits:
                    tmp = []
                    for alpha in dicts[i]:
                        for v in result:
                            tmp.append(v+alpha)
                    result = tmp
                return result
