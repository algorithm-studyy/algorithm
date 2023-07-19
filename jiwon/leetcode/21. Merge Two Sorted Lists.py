# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        head = answer = ListNode()
        while list1 or list2:
            if not list2 or (list1 and list2 and list1.val <= list2.val):
                answer.next, list1 = ListNode(list1.val), list1.next
            elif not list1 or (list1 and list2 and list1.val > list2.val):
                answer.next, list2 = ListNode(list2.val), list2.next
            answer = answer.next
        return head.next