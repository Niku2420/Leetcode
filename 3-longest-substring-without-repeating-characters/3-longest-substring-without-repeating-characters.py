class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        res=0
        for i in range(len(s)):
            while (s[i] in charset):
                charset.remove(s[l])
                l+=1
            charset.add(s[i])
            res=max(res,i-l+1)
        return res
        