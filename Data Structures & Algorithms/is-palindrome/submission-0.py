class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s=s.lower()
        st=""
        if n == 1 :
            return True 
        for i in s :
            if i.isalnum()==True :
                st+=i
            else :
                st+=""
        l=0
        r=len(st)-1
        while l <= r :
            if st[l]==st[r]:
                r-=1
                l+=1
            else :
                return False 
        return True 
        
                