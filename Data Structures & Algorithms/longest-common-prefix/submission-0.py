class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(len(s) for s in strs)
        prefix = ""
        n = len(strs)
        for i in range(smallest):
            for j in range(1,n):
                if strs[j][i]!=strs[0][i]:
                    return prefix 
            prefix+=strs[0][i]
        return prefix 