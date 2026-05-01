class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        nums.sort()
        longest = curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                # consecutive
                curr += 1
            elif nums[i] == nums[i-1]:
                # duplicate
                pass
            else:
                # streak broken
                curr = 1

            longest = max(curr, longest)
                
        return longest