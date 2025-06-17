# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        stack=[slow.val]
        while slow.next:
            slow=slow.next
            stack.append(slow.val)
        while stack:
            if stack.pop()!=head.val:
                return False
            head=head.next
        return True
        