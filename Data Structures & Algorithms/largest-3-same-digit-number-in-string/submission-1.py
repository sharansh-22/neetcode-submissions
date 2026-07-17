class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        numn=""
        for i in range(n-2):
            candidate=""
            if num[i]==num[i+1]==num[i+2]:
                candidate+=num[i:i+3]
            if candidate > numn :
                numn=candidate
        return numn
        