# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(a: ListNode, b: ListNode):
    dummy = temp = ListNode()

    while a and b:
        if a.val < b.val:
            temp.next = a
            a = a.next
        else:
            temp.next = b
            b = b.next
        temp = temp.next

    temp.next = a or b

    return dummy.next
