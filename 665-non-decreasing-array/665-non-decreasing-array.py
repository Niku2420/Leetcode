class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        diff=0
        for i in range(1,len(nums)):
            prev,cur=nums[i-1],nums[i]
            if prev>cur:
                diff+=1
                if i<2 or nums[i-2]<=cur:
                    nums[i-1]=cur
                else:
                    nums[i]=prev
        return diff<=1
    # return diff<=-1

    
            
        
        