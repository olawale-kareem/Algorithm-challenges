class Node:
    def __init__(self,data):
        self.data = data
        self.nextval = None
class LinkedList:
    def __init__(self):
        self.head = None
    def at_beginning(self, new_data):
        new_node = Node(new_data)     
        new_node.nextval = self.head # Head -> Node 21 -> None # Head -> Node22 -> Node 21 -> None
        self.head = new_node
    def at_end (self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head   # Node(data-> 22, Node21) -> Node (data-> None)
        while (last_node.nextval):
            last_node = last_node.nextval # Node (21 -> None)
        last_node.nextval = new_node # Node(data-> 22, Node21) -> Node (data-> Node(the end))-> Node(the end -> None)

    def print_all(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.nextval
# ----------------------------------------------------------------------------
# linked list 
# reversed link list method added

class Node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return 'Node data: %s',self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        curr = self.head
        count = 0
        while curr:
            cur = curr.next_node
            count += 1
        return count

    def search(self,key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            else:
                curr = curr.next_node
        return None

    def insert(self, data, index):

        if index == 0:
            self.add(data)
        else:
            new_element = Node(data)
            position = index
            curr = self.head

            while position > 1:
                curr = curr.next_node
                position -= 1

            prev_node = curr
            new_next_node = curr.next_node

            prev_node.next_node = new_element
            new_element.next_node = new_next_node

    
    def remove(self,key):
        curr = self.head
        prev_element = None
        found  = False

        while curr and not found:
            if curr.data == key and curr == self.head:
                found = True
            elif curr.data == key:
                found = True
                prev_element.next_node = curr.next_node
            else:
                prev_element = curr
                curr = curr.next_node

        return curr


    def reversed_array(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next_node
        reversed_nodes = nodes[::-1]
        return '<-'.join(reversed_nodes)


    def __repr__(self):
        nodes = []
        curr = self.head
        
        while curr:
            if curr is self.head:
                nodes.append('Head: %s' % curr.data)

            elif curr.next_node is None:
                nodes.append('Tail: %s' % curr.data)

            else:
                nodes.append('%s' %  curr.data)

            curr = curr.next_node

        return '->'.join(nodes)


    def reversed_array(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next_node
        reversed_nodes = nodes[::-1]
        return '<-'.join(reversed_nodes)


l = LinkedList()
l.add(9)
l.add(10)
l.add(11)
l.add(13)

print(l.reversed_array())

