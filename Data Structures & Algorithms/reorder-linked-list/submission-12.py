# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 1 -> 2 -> 3 -> 4 -> 5
        # s=f=1 -> s=2,f=3 -> s=3,f=5

        # reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # the way that works:
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # slow = 3, slow.n = 4 => sec = 4 -> 5 -> None, prev=slow.n=None
        # 1 -> 2 -> 3 -> None (sec = 4 -> 5 -> None)
        # first iter:
        # tmp = sec.n = 5 -> None
        # sec.n = None (sec = 4 -> None)
        # prev = sec = 4, sec = tmp = 5
        # head = 1 -> 2 -> 3 -> None, prev = 4 -> None, second = 5 -> None
        # second iter:
        # tmp = sec.next = None
        # sec.next = prev => 5 -> 4 -> None
        # prev = sec = 5 -> 4 -> None
        # sec = tmp = None (stops iter)
        # head = 1 -> 2 -> 3 -> None, prev = 5 -> 4 -> None
        
        # what if second = slow ? (so we actually split up the array like 1 -> 2 + 3 -> 4 -> 5)
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # prev = None, second = slow (3)
        # while sec: (first iter)
        # tmp = sec.next (4)
        # sec.next = None => 3 -> None
        # prev = 3, sec = 4
        # second iter:
        # tmp = 5
        # sec.next = 3 => 4 -> 3 -> None
        # prev = 4, sec = 5
        # third iter:
        # tmp = None
        # sec.next = 4 => 5 -> 4 -> 3 -> None
        # prev = sec (5), sec = None
        # head = 1 -> 2 -> 3 -> 4 -> 5 <=== This is the problem, need to re-assign 2.next = None
        # prev = 5 -> 4 -> 3 -> None

        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        # first = 1 -> 2 -> 3 -> None, sec = 5 -> 4 -> None
        # first iter:
        # tmp1 = 2 -> 3 -> None, tmp2 = 4 -> None
        # first.next = 5 => head = 1 -> 5 -> 4 -> None
        # second.next = 2 => head = 1 -> 5 -> 2 -> 3 -> None
        # first = 2 -> 3 -> None, sec = 4 -> None
        # second iter:
        # tmp1 = 3 -> None, tmp2 = None
        # first.next = 4 => head = 1 -> 5 -> 2 -> 4 -> None
        # second.next = 3 => head = 1 -> 5 -> 2 -> 4 -> 3 -> None
        # first = 3, sec = None (stops iter)
        # head = 1 -> 5 -> 2 -> 4 -> 3 -> None :)
