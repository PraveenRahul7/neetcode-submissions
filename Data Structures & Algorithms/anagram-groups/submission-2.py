class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        res = list()
        for word in strs:
            key = tuple(sorted(word))
            if key not in seen:
                seen[key]=list()
            seen[key].append(word)
        
        for key,value in seen.items():
            res.append(value)
        return res


        