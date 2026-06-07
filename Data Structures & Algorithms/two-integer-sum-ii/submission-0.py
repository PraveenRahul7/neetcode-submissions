class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<2:
            return []
        i,j = 0, len(numbers)-1
        while i<j and numbers[i]+numbers[j]!=target:
            if numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        return [i+1,j+1]
        
        