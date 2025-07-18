class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num=2
        ana=defaultdict(list)
        for i in strs:
            sot="".join(sorted(i))
            ana[sot].append(i)
        return list(ana.values())