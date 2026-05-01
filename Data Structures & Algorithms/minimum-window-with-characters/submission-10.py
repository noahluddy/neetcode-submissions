class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        
        L = 0
        length = float('inf')
        t_chars, window = Counter(t), Counter()
        have, need = 0, len(t_chars) # num of unique chars in t
        res = [-1, -1]

        for R in range(len(s)):
            window[s[R]] += 1
            if window[s[R]] == t_chars[s[R]]:
                have += 1
            while have == need:
                if (R - L + 1) < length:
                    res = [L, R + 1]
                    length = R - L + 1
                window[s[L]] -= 1
                if s[L] in t_chars and window[s[L]] < t_chars[s[L]]:
                    have -= 1
                L += 1

        return '' if length == float('inf') else s[res[0]:res[1]]