class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxr = arr[-1]
        n = len(arr)
        for i in range(n - 1, -1, -1):
            temp=arr[i]
            arr[i]=maxr
            maxr=max(temp,maxr)
        arr[-1]=-1
        return arr