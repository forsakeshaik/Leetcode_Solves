class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True
        
        s_pointer = 0

        for letter in t:
            if s_pointer < s_len and letter == s[s_pointer]:
                s_pointer += 1
            
            if s_pointer == s_len:
                return True