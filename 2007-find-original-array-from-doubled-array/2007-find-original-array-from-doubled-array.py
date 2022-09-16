class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count, result = Counter(changed), []
        for num in sorted(changed, key = lambda x: abs(x)):
            if count[num] == 0: 
                continue
            if count[2*num] == 0: 
                return []
            result += [num]
            
            if num == 0 and count[num]<= 1: 
                return []
            count[num] -= 1
            count[2*num] -= 1
        
        return result
    
    
            
        
                
                
        