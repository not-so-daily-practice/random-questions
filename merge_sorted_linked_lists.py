class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


list1 = Node(0)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(6)
list1.next.next.next.next = Node(8)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(5)
list2.next.next.next = Node(7)


def merge(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.data < list2.data:
        list1.next = merge(list1.next, list2)
        return list1
    else:
        list2.next = merge(list2.next, list1)
        return list2


merged = merge(list1, list2)

while merged.next is not None:
    print(merged.data)
    merged = merged.next
