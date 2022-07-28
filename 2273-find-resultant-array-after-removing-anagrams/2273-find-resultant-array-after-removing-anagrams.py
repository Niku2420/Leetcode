class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for i in range(len(words)):
            #check anagram
            if sorted(res[-1])!=sorted(words[i]):
                res.append(words[i])
        return res      