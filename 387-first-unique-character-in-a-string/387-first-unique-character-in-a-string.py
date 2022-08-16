class Solution:
    def firstUniqChar(self, s: str) -> int:
        dt={}
        for i in s:
            if i not in dt:
                dt[i]=1
            else:
                dt[i]+=1
        for i in range(len(s)):
            if dt[s[i]]==1:
                return i
        return -1
        
                
                
            
            
            
        