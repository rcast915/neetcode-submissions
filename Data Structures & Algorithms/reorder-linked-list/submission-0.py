# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into two
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # Reverse second list
        newll = None
        curr = head2

        while curr:
            currnext = curr.next
            curr.next = newll
            newll = curr

            curr = currnext
        
        
        final = head
     
        while head and newll:
            headnext = head.next
            head.next = newll

            newllnext = newll.next
            newll.next = headnext

            head = headnext
            newll = newllnext
            
        

        return final
            






        