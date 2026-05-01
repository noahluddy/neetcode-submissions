class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i = 0
        for color, count in enumerate(counts):
            for _ in range(count):
                nums[i] = color
                i += 1
                