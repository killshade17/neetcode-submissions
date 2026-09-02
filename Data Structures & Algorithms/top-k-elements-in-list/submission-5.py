class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        arr = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            res[nums[i]] = 1 + res.get(nums[i], 0)
        for num, count in res.items():
            arr[count].append(num)

        sol = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
