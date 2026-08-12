class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        res=list()
        nums.sort()
        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            low, high=i+1,n-1
            while low<high:
                three_sum=num+nums[low]+nums[high]
                if three_sum<0:
                    low+=1
                elif three_sum>0:
                    high-=1
                else:
                    res.append([num, nums[low], nums[high]])
                    low+=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
        return res

        