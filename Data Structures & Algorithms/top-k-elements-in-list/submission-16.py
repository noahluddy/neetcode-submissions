# O(n) T, O(n) S

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        for count in range(len(freq) - 1, 0, -1):
            # if freq[count]:
            #     result.extend(freq[count])
            #     k -= len(freq[count])
            #     if k <= 0:
            #         return result
            for num in freq[count]:
                result.append(num)
                if len(result) == k:
                    return result
