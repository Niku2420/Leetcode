#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    idx=binarysearch(arr,n,x)
	    if idx==-1:
	        return 0
	    k=1
	    left=idx-1
	    while (left>=0 and arr[left]==x):
	        k+=1
	        left-=1
	    right=idx+1
	    while (right<n and arr[right]==x):
	        k+=1
	        right+=1
	    return k
	            
def binarysearch(arr,n,x):
    l=n-1
	s=0
	while s<=l:
	    m=(s+l)//2
	    if arr[m]==x:
	       return m
	    elif arr[m]<x:
	       s=m+1
	    else:
	       l=m-1
    return -1
    
	    
	    
	        
	        
	        
	        
	        
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends