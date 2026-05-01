class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]

        left_prods = []
        running_left_prod = 1
        for num in nums:
            running_left_prod *= num
            left_prods.append(running_left_prod)
        
        right_prods = [0] * len(nums)
        running_right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            running_right_prod *= nums[i]
            right_prods[i] = running_right_prod

        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[i] = right_prods[i + 1]
            elif i == len(nums) - 1:
                result[i] = left_prods[i - 1]
            else:
                result[i] = left_prods[i - 1] * right_prods[i + 1]

        return result