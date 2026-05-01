class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = []
        if len(set(nums)) < len(nums):
            return True
        else: return False