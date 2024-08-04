class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
            

        #set_map = []
        #letters = list(s)
        #s1 = ' '

        #for i in letters:
            #if i in set_map:
               # return (len(s1))
            #set_map.append(i)
            #s1 = ''.join(set_map)
        