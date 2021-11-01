# from class_based_algorithms.linked_list import LinkedList

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
                nodes.append('[Head: %s]' % curr.data)

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

    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                currenr = current.next_noden 
                position += 1
            return current

linked_list = LinkedList()

def split(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid -1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half

def merge(left,right ):
    merged = LinkedList()
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif  right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
            current = current.next_node
        head = merged.head.next_node
        merged.head = head
        return merged

def linked_list_merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half =split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right )