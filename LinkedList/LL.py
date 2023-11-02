
class Node:

    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class LinkedList:

    global length

    def __init__(self, value=0):

        self.length = 1

        # Pythonic way to Overload the Constructor!
        if type(value) is list:
            self.head = Node(value[0])
            for n in value[1:]:
                self.append(n)

        else:
            self.head = Node(value)



    # Without the global length, this function was doing the job.

    # def leng(self):
    #     counter = 1
    #     temp = self.head
    #     while temp.next:
    #         counter += 1
    #         temp = temp.next
    #     return counter

    # Now updating the length counter as it's appended, inserted or removed.
    def leng(self):
        return f'The length of the Linked List is: {self.length}'
    def append(self, value):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)
        self.length += 1

    def nodeAppend(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node


    def insert(self, value):
        temp = Node(value, self.head)
        self.head = temp
        self.length += 1

    def pr(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

# # Initiating the Linked List
# LL = LinkedList(1)
#
# # Appending the Linked List at the end.
# LL.append(3)
# LL.append(4)
# LL.append(5)
# LL.append("Bilal")
#
# # Inserting before the head of the Linked List (i.e. this is the new head).
# LL.insert(2)
#
# # Printing the length of the Linked List.
# print(LL.leng())
