class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for i in nums :
            map[i]=map.get(i,0)
            map[i]+=1
        if len(map.values()) < sum(map.values()):
            return True 
        else :
            return False