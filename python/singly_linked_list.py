class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")

            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.append(7)
    llist.append(1)
    llist.append(4)

    llist.print_list() 