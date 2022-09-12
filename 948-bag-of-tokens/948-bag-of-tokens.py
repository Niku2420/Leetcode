class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens=sorted(tokens)
        beg=0
        end=len(tokens)-1
        score=0
        max_S=0
        while beg<=end:
            if tokens[beg]<=power:
                power-=tokens[beg]
                score+=1
                max_S=max(max_S,score)
                beg+=1
            elif score>=1:
                power+=tokens[end]
                score-=1
                end-=1
            else:
                break
        return max_S
                
        
                
            
            
            
                
            
            
        