class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars = Counter(t)
        def is_valid_substring(sub: str) -> bool:
            return t_chars <= Counter(sub)
        
        min_sub, len_min_sub = '', float('inf')
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if len(sub) < len_min_sub and is_valid_substring(sub):
                    len_min_sub = len(sub)
                    min_sub = sub

        return min_sub
