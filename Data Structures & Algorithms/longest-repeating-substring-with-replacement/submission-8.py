# O(n) T, O(m) S -> O(26) S -> O(1) S

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res