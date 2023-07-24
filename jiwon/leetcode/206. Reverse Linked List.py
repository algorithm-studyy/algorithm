# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        head = listNode = ListNode()
        for i in lst[::-1]:
            node = ListNode(i)
            listNode.next = node
            listNode = listNode.next
        return head.next