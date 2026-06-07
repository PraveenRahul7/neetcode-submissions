class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() #t->nlog(n); s-> o(n) worst case
        res, currSum = 1,1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==1+nums[i-1]:
                currSum+=1
            else:
                currSum = 1
            res = max(res, currSum)
        return res if nums else 0
