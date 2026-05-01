class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        productL, productR = 1,  1
        for l in range(len(nums)):
            res[l] = productL
            productL *= nums[l]
        
        for r in range(len(nums) - 1, -1, -1):
            res[r] *= productR
            productR *= nums[r]
        
        return res