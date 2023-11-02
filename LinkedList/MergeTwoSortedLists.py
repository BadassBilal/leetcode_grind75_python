#Definition for singly-linked list.

from LL import *

def mergeTwoSortedLists(a, b):

    temp = LinkedList()

    while a and b:
        if a.val < b.val:
            temp.append(a.val)
            a = a.next
        else:
            temp.append(b.val)
            b = b.next

    temp.nodeAppend(a) if a else temp.nodeAppend(b)

    return temp




def main():
    LL1 = LinkedList([10,20,30,40])
    LL2 = LinkedList([5,15,45,50,55])
    LLR = mergeTwoSortedLists(LL1.head, LL2.head)
    LLR.pr()



if __name__ == "__main__":
    main()