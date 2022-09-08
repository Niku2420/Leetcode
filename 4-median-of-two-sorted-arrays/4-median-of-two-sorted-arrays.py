class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        t=len(nums)
        if t%2==0:
            return (nums[int(t/2)] + nums[int(t/2-1)]) / 2
        else:
            
            return nums[t//2]
        
        