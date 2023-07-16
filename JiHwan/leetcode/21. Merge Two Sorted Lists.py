# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        while list1:
            l1.append(list1.val)
            list1 = list1.next
        while list2:
            l2.append(list2.val)
            list2 = list2.next

        merged_list = sorted(l1 + l2)  # 리스트를 정렬하여 merged_list에 저장

        # 정렬된 리스트를 연결 리스트로 변환
        head = ListNode()
        current = head
        for value in merged_list:
            current.next = ListNode(value)
            current = current.next

        return head.next


