from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result, counters = [], []
        for s in strs:
            if Counter(s) in counters:
                for anagrams in result:
                    if Counter(s) == Counter(anagrams[0]):
                        anagrams.append(s)
            else:
                counters.append(Counter(s))
                result.append([s])
        return result
