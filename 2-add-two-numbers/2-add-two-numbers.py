class listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    
    def addTwoNumbers(self,l1: listnode,l2: listnode) -> listnode:
        n1,n2="",""
        while l1:
            n1=str(l1.val)+n1
            l1=l1.next
        while l2:
            n2=str(l2.val)+n2
            l2=l2.next
        if not n1:
            n1="0"
        if not n2:
            n2="0"
        summ=int(n1)+int(n2)        
        dummy=cur=listnode()
        for i in reversed(str(summ)):
            cur.next=listnode(int(i))
            cur=cur.next
        return dummy.next
        