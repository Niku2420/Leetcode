class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r,N=matrix[0][0],matrix[-1][-1],len(matrix)
        def less_k(m):
            count=0
            
            for i in range(N):
                x=bisect_right(matrix[i],m)
                count+=x
            return count
        while l<r:
            mid=(l+r)//2
            if less_k(mid)<k:
                l=mid+1
            else:
                r=mid
        return l
    
                
                
        
        