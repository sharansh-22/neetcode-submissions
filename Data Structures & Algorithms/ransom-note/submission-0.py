class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for i in magazine:
            hashmap[i]=hashmap.get(i,0)
            hashmap[i]+=1
        for i in ransomNote :
            if hashmap.get(i,0) == 0 :
                return False 
            hashmap[i]-=1
        return True 
