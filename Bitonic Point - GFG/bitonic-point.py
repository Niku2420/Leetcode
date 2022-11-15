#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
	    if n==1:
	        return arr[1]
		maxNum=list()
# 		maxNum.append(arr[1])
		for i in range(1,len(arr)-1):
		    if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
		        if not maxNum:
		            maxNum.append(arr[i])
		        else:
		            if maxNum[-1]<arr[i]:
		                maxNum.pop()
		                maxNum.append(arr[i])
	    if maxNum :
	        return maxNum[-1]
	    else:
	        return n
	    
	
	   
	   
	    
		        
		        
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends