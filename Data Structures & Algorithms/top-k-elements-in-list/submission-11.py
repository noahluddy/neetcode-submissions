class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i]:
                result.extend(freq[i])
                k -= len(freq[i])
                if k <= 0:
                    return result
