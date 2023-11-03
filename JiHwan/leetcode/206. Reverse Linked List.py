# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headList = []
        while head:
            headList.append(head.val)
            head = head.next
        head_reversed = headList[::-1]

        head = ListNode()
        current = head
        for value in head_reversed:
            current.next = ListNode(value)
            current = current.next

        return head.next

