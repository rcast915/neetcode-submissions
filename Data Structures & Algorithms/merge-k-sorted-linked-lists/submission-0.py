
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        
        def mergelist(a: List[Optional[ListNode]], b: List[Optional[ListNode]]):
            
            if a is None or b is None:
                if a is None and b is None: return
                return a or b
            
            
            fakehead = ListNode(0, None)
            curr = fakehead

            while a and b:
                if a.val <= b.val:
                    curr.next = a

                    curr = curr.next
                    a = a.next
                else:
                    curr.next = b

                    curr = curr.next
                    b = b.next
            
            curr.next = a or b

            return fakehead.next
        
        if len(lists) == 0: return
        if len(lists) ==  1: return lists[0]

        elif len(lists) == 2: return mergelist(lists[0], lists[1])
        
        else: 
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return mergelist(left, right)