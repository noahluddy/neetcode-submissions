class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[hi]:
                hi = mid # keep mid in range
            else:
                lo = mid + 1
        pivot = lo

        # hi can't equal the pivot (which is the min!!!)
        # lo, hi = 0, len(nums) - 1
        # if target > nums[pivot] and target <= nums[hi]:
        #     lo = pivot + 1
        # else:
        #     hi = pivot
        lo, hi = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[hi]:
            lo = pivot
        else:
            hi = pivot - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid

        return -1