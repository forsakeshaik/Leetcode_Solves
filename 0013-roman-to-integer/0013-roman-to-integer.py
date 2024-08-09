class Solution(object):
    def romanToInt(self, s):
        m = {
           'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000
        }

        rom = 0
        for i in range(len(s)):
            if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
                rom -=m[s[i]]
            else:
                rom +=m[s[i]]
        return rom
        