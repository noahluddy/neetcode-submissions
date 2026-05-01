class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = set(s)
        for c in chars:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                if (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res

# O(26n) -> O(n) T, O(26) S -> O(1) S