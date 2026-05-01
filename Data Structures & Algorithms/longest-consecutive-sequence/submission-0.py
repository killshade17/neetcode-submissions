class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in store:
                length = 0
                while (n + length) in store:
                    length += 1
                longest = max(length, longest)
        return longest
        