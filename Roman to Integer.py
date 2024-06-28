class Solution:
    def romanToInt(self, s):
        Roman={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,
               "CD":400,"D":500,"CM":900,"M":1000}
        integer=0
        i=0
        while (i<len(s)):
            if s[i:i+2] in Roman:
                integer+=Roman[s[i:i+2]]
                i+=2
            else:
                integer+=Roman[s[i]]
                i+=1
        return integer
