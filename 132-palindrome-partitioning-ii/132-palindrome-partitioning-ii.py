class Solution:
    def minCut(self, s: str) -> int:
        dp=[float('inf')]*len(s)
        is_panlindrome=[[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[i]==s[j] and (i-j<2 or is_panlindrome[j+1][i-1]):
                    is_panlindrome[j][i]=True
                    dp[i]=0 if j==0 else min(dp[i],dp[j-1]+1)
        return dp[len(s)-1]
        