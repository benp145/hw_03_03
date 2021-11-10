
class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f'<Node: {self.data}>'

    # getters
    def get_data(self):
        return self.data

    def get_prev_node(self):
        return self.prev_node

    def get_next_node(self):
        return self.next_node

    # setters
    def set_data(self, new_data):
        self.data = new_data

    def set_prev_node(self, node):
        self.prev_node = node

    def set_next_node(self, node):
        self.next_node = node


class DoublyLinkedList:
    def __init__(self, root=None, end=None):
        self.root = root
        self.end = end
        self.size = 0

    #getters
    def get_root(self):
        return self.root

    def get_end(self):
        return self.end

    def get_size(self):
        return self.size

    def add_to_front(self, data):
        new_node = Node(data, next_node=self.root)
        self.root = new_node
        self.size += 1 
        if self.size == 1:
            self.end = new_node
        elif self.size == 2:
            self.end = self.root.next_node
    
    def add_to_back(self, data):
        new_node = Node(data, prev_node=self.end)
        self.end = new_node
        self.size += 1
        if self.size == 1:
            self.root = new_node
        elif self.size == 2:
            self.root = self.end.prev_node
        

    def remove(self, data):
        this_node = self.root
        p_node = None
        n_node = this_node.get_next_node()

        while this_node:
            if this_node.get_data() == data:
                if p_node:
                    p_node.set_next_node(this_node.get_next_node())
                if n_node:
                    n_node.set_prev_node(this_node.get_prev_node())
                self.size -= 1
                return True
            else:
                p_node = this_node
                this_node = this_node.get_next_node()
                n_node = n_node.get_next_node()
        return False    

    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return this_node
            else:
                this_node = this_node.get_next_node()
        return None

l = DoublyLinkedList()
l.add_to_front(9)
l.add_to_back(4)
l.add_to_front(7)
l.add_to_front(3)
l.add_to_front(22)
l.add_to_back(5)
print(l.find(3))
print(l.get_end())
print(l.get_root())
print(l.get_size())
print(l.remove(3))
print(l.find(3))
print(l.get_size())

        

    