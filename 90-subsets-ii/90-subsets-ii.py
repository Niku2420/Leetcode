class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        subset=[[]]
        for n in nums:
            for i in range(len(subset)):
                currentSubset=subset[i]
                newSubset=currentSubset+[n]
                if newSubset not in subset:
                    subset.append(newSubset)
        return subset
    
        
        
                