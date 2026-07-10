class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs={}
        for i in s :
            hashs[i]=hashs.get(i,0)
            hashs[i]+=1
        hasht={}
        for i in t :
            hasht[i]=hasht.get(i,0)
            hasht[i]+=1
        if hasht==hashs:
            return True 
        else :
            return False 