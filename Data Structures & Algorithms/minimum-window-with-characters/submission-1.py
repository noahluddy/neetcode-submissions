class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid_substring(sub: str) -> bool:
            t_chars = Counter(t)
            for c in sub:
                t_chars[c] -= 1
            return not +t_chars
        
        min_sub, len_min_sub = '', float('inf')
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if len(sub) < len_min_sub and is_valid_substring(sub):
                    len_min_sub = len(sub)
                    min_sub = sub

        return min_sub

# Brute Force: O(n^3 + n^2 * m) T, O(n + m) S