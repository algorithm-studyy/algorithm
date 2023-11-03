# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = []
        for lst in lists:
            while lst:
                merged_list.append(lst.val)
                lst = lst.next
        result = head = ListNode()
        for val in sorted(merged_list):
            result.next = ListNode(val)
            result = result.next
        return head.next