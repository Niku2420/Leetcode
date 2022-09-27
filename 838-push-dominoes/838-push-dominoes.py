class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom=list(dominoes)
        ans=""
        q=deque()
        for i,d in enumerate(dom):
            if d!=".":
                q.append((i,d))
        while q:
            i,d=q.popleft()
            if d=="L" and i>0 and dom[i-1]==".":
                q.append((i-1,"L"))
                dom[i-1]="L"
            elif d=="R":
                if i+1 <len(dom) and dom[i+1]==".":
                    if i+2<len(dom) and dom[i+2]=="L":
                        q.popleft()
                    else:
                        q.append((i+1,"R"))
                        dom[i+1]="R"
        
        return ans.join(dom)         

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         stack=[]
#         i=0
#         while i<len(dominoes):
#             if dominoes[i]==".":
#                 stack.append(".")
#                 i+=1
#             elif dominoes[i]=="L":
#                 if stack and stack[-1]==".":
#                     stack.pop(-1)
#                     stack.append("L")
#                     stack.append("L")
#                     i+=1
#                 else:
#                     stack.append("L")
#                     i+=1
#             else:
#                 if dominoes[i+1]:
#                     if dominoes[i+1]==".":
#                         stack.append("R")
#                         stack.append("R")
#                         i+=1
#                     else:
                    
#                         i+=1
#         return stack
        