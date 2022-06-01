class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        arr=[]
        for i in range(len(nums)):
            total+=nums[i]
            arr.append(total)
        return arr
            