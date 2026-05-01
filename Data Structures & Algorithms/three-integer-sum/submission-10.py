# O(n^2) T, O(1) S

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                test = num + nums[left] + nums[right]
                if test == 0:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                elif test < 0:
                    left += 1
                else:
                    right -= 1
                
        return [list(tup) for tup in result]
