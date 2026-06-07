class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        res = list()
        for word in strs:
            key = tuple(sorted(word))
            if key not in groups:
                groups[key]=list()
            groups[key].append(word)
        for key, value in groups.items():
            res.append(value)
        return res
        