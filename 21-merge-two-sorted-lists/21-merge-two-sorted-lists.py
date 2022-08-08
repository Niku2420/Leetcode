# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        p1=list1
        p2=list2
        prev=None
        
        while p1 is not None and p2 is not None:
            if p1.val<=p2.val:
                prev=p1
                p1=p1.next
                
                
            else:
                if prev is not None:
                    prev.next=p2
                prev=p2
                p2=p2.next
                prev.next=p1
        if p1 is None:
            prev.next=p2
        return list1 if list1.val<=list2.val else list2
                
                
                    
        
        
        