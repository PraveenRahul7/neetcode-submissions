from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = Counter()
        i, j = 0, 0
        res = 0
        while j<n:
            count[s[j]]+=1
            while len(count)<j-i+1:
                count[s[i]]-=1
                if count[s[i]]==0:
                    del count[s[i]]
                i+=1
            if len(count)==j-i+1:
                res = max(res, j-i+1)
            j+=1
        return res    