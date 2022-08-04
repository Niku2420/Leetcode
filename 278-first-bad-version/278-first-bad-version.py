# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            result=isBadVersion(mid)
            
            if result==True:
                right=mid-1
            elif result==False:
                left=mid+1
            else:
                return result
        return left
            
        
        
        