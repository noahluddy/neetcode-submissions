# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2 if list2 else None
        elif not list2:
            return list1
        
        head = list1 if (list1 and list1.val < list2.val) else list2
        res = head
        if head == list1:
            list1 = list1.next
        else:
            list2 = list2.next
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return res

# 1 2 4 + 1 3 5
# head = 1 (from 1 3 5)
# list1 = 1 2 4
# list2 = 3 5
# while list1 and list2:
#   head.next = 1 (from 1 2 4)
#   list1 = 2 4
#   head = 1 (from 1 2 4)
#   - l1 = 2 4, l2 = 3 5
#   head.next = 2 (h=1 1 2)
#   list1 = 4
#   head = 2
#   - ...
#   head.next = 4 (1 1 2 3 4)
#   list1 = None
#   head = 4
#   - elif list2:
#   head.next = (5 -> None)
