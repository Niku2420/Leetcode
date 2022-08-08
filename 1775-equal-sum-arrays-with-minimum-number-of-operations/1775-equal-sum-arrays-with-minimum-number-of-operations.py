class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum_nums1=sum(nums1)
        sum_nums2=sum(nums2)
        if sum_nums1>sum_nums2:
            nums1,nums2=nums2,nums1
        if 6*len(nums1)<len(nums2):
            return -1
        nums1=[6-num for num in nums1]

        nums2=[num-1 for num in nums2]
        
        diff=abs(sum_nums1-sum_nums2)
        
        ops=sorted(nums1+nums2,reverse=True)
        print(ops,diff)
        result=0
        for r in ops:
            if diff<=0:
                break
            result+=1
            diff-=r
        return result
        