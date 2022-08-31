class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(1,(len(s)//2)+1):
            if s==s[i:]+s[:i]:
                return True
        return False
        
        
            
            
            
        