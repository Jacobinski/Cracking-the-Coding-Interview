class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class Linked_List:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        node = Node()
        node.value = data
        node.next = self.cur_node
        self.cur_node = node

    def lprint(self):
        node = self.cur_node
        while node != None:
            print(node), # This comma is weird. It lets you print on the same line
            node = node.next
        print("")

    def remove_dups(self):
        # Start runner at same place as reader
        reader = self.cur_node
        runner = self.cur_node

        # Reader is none at the end of the list
        while reader != None:
            value = reader.value
            runner = reader
            query = runner.next

            # Runner is none at the end of the list
            while query != None:
                # Check to see if next item is duplicate
                if query.value == value:
                    runner.next = runner.next.next # Point the list to skip query
                    query.next = None # Remove to query's assocation
                    query = runner.next # Get a new query
                else:
                    runner = runner.next
                    query = runner.next

            reader = reader.next

list = Linked_List()
list.add_node(1)
list.add_node(2)
list.add_node(3)
list.add_node(4)
list.add_node(8)
list.add_node(8)
list.add_node(4)
list.add_node(8)
list.add_node(1)
list.add_node(4)
list.add_node(9)
list.add_node(6)

list.lprint()

list.remove_dups()

list.lprint()