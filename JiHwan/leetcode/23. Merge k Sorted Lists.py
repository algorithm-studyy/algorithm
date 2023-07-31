# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []

        for list in lists:
            while list:
                data.append(list.val)
                list = list.next
        result = sorted(data)

        head = ListNode()
        current = head
        for value in result:
            current.next = ListNode(value)
            current = current.next

        return head.next