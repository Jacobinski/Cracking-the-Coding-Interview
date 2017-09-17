class Node:
    def __init__(self, cargo = None):
        self.cargo = cargo
        self.next = None

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add(self, cargo):
        new_node = Node(cargo)
        new_node.next = self.cur_node
        self.cur_node = new_node

    def __str__(self):
        string = "["
        node = self.cur_node
        while node is not None:
            string += " " + str(node)
            node = node.next
        string += " ]"
        return string

    def return_Kth_to_last(self, k):
        def Kth_to_last(node, k):
            head = node
            tail = node.next
            if tail is None:
                value, length = None, 0
            else:
                value, length = Kth_to_last(tail, k)
                length += 1

            if k == length:
                value = head.cargo

            return value, length

        value, length = Kth_to_last(self.cur_node, k)
        return value

ll = LinkedList()
for i in range(10):
    ll.add(i)
print(ll)

for i in range(10):
    value = ll.return_Kth_to_last(i)
    if value is None:
        print("Got none")
    else:
        print(str(value))
