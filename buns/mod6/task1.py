class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        current_node = self.head
        if not isinstance(self.head, Node):
            self.head = new_node
            return
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def __str__(self):
        current_node = self.head
        line = ""
        while current_node != None:
            line += str(current_node.get_data()) + ' '
            current_node = current_node.get_next()
        return line

    def get(self, index):
        new_node = self.head
        el_index = 0
        while el_index <= index:
            if el_index == index:
                return new_node.get_data()
            el_index += 1
            new_node = new_node.get_next()

    def push_front(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def insert(self, index, data):
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node.get_next() != None:
            if index in [0, 1]:
                self.push_front(data)
                return
            elif count + 1 == index:
                next_node = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(next_node)
                return
            count += 1
            current_node = current_node.get_next()



