class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

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
            print(str(node.value)), # This comma is weird. It lets you print on the same line
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

            # Runner is none at the end of the list
            while runner.next != None:
                # Check to see if next item is duplicate
                if runner.next.value == value:
                    # Remove the item & get new next
                    runner.next = runner.next.next
                else:
                    runner = runner.next

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