# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 : return head   

        def reverse(head):
            newll = None
            curr = head

            while curr:
                nextNode = curr.next

                curr.next = newll
                newll = curr

                curr = nextNode
            return  newll, head
        

        fakehead = ListNode(0, head)
        prev = fakehead
        curr = head
        count = 1

        while curr:
            if count == 0:
                nextnode = curr.next

                curr.next = None

                head, tail = reverse(khead)
                prev.next = head
                tail.next = nextnode

                curr = tail 
                prev = tail

            elif count == 1:
                khead = curr


            curr = curr.next
            count = (count + 1) % k

        return fakehead.next


        