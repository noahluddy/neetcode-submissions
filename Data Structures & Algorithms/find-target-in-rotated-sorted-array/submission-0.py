class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]: # right portion is rotated
                hi = mid # keep mid in the range
            else:
                lo = mid + 1
        pivot = lo
        lo_res = self.bsearch(nums, 0, pivot - 1, target)
        hi_res = self.bsearch(nums, pivot, len(nums) - 1, target)
        if lo_res != -1:
            return lo_res
        elif hi_res != -1:
            return hi_res
        return -1
    
    def bsearch(self, nums: List[int], lo: int, hi: int, target: int) -> int:
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        return -1