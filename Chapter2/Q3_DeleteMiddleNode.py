class Node:
    def __init__(self, cargo = None):
        self.cargo = cargo
        self.next = None

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self):
        self.cur_node = None

    def __str__(self):
        string = "["
        node = self.cur_node
        while node is not None:
            string += " " + str(node)
            node = node.next
        string += " ]"
        return string

    def add(self, cargo):
        new_node = Node(cargo)
        new_node.next = self.cur_node
        self.cur_node = new_node

    def delete_middle_node(self, node):
        # Lets make our node look like the next one, and
        # delete that one instead
        middle_node = node
        to_delete_node = node.next

        middle_node.cargo = to_delete_node.cargo
        middle_node.next = to_delete_node.next
        to_delete_node.next = None

    def get_node(self, value):
        search = self.cur_node
        while search:
            if search.cargo == value:
                return search
            search = search.next
        return None

ll = LinkedList()
for i in range(10):
    ll.add(i)

print(ll)

node = ll.get_node(5)

ll.delete_middle_node(node)

print(ll)