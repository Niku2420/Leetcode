class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D1={}
        D2={}
        for i in s:
            if i not in D1:
                D1[i]=1
            else:
                D1[i]+=1
        for i in t:
            if i not in D2:
                D2[i]=1
            else:
                D2[i]+=1
        return D1==D2
        