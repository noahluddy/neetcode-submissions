# O(n * m) T, O(n) S
# n == num of strings, m == length of longest string

from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            counts[tuple(count)].append(s)
        return list(counts.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         counts = defaultdict(list)
#         for s in strs:
#             count = Counter(s)
#             counts[count].append(s)
#         return list(counts.values())
