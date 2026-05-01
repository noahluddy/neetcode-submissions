class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        k_most_frequent = sorted(counts.values())[-k:]

        result = set()
        for count in k_most_frequent:
            for num, val in counts.items():
                if count == val:
                    result.add(num)

        return list(result)