class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com=(strs[0])
        for i in strs[1:]:
            lo=[]
            while not i.startswith(com):
                com=com[:-1]
                if not com:
                    return ""
        return com