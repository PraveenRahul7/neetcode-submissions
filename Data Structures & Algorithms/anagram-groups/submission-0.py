class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = list()
        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)
        for key, value in groups.items():
            res.append(value)
        return res
        