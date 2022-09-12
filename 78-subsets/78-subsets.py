class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[[]]
        for ele in nums:
            for i in range(len(subset)):
                currentSubset=subset[i]
                subset.append(currentSubset+[ele])
        return subset
        