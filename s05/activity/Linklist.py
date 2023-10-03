#Output should be [ 6 , 4, 3, 2, 1 ]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                # 1st Loop: head.next = current.next
                current = current.next
                # 2nd Loop: current.next.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def swap(self):
        if self.head is None or self.head is None or self.head.next.next is None:
            return

        SecondNode= self.head.next
        ThirdNode = SecondNode.next
        SecondNode.data, ThirdNode.data = ThirdNode.data, SecondNode.data


my_linked_list = LinkedList()

input_values = [6, 3, 4, 2, 1]
my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

my_linked_list.swap()
my_linked_list.display()
