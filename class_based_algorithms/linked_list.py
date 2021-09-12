class Node:
    
    # the doc-string
    '''
    This is a linked list example
    This models two attributes- the data and the link to the next node in the list
    '''
    # initially instantiated  parameters
    data = None
    next_node = None
    
    # the node class takes "data" as a default parameter
    def __init__(self, data):
        self.data = data
    
    # this is to edit the object representation better when any Node is called.
    def __repr__(self):
        return "Node data: %s" %self.data

 
class LinkedList:  
    '''
    singly linked list
    '''
    # initializing a list head
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    

    def size(self):
        ''' returns the size of our list in linear time'''
        # current node 
        # matches the immediate node head  
        current = self.head
        # current count
        count = 0
        # use while loop to count backwards till we reach the tail with the "None" value
        while current != None:
            count +=1
            current = current.next_node
        return count

    def add(self, data):
        '''
        This new node contains data at the list
        takes O(1)
        '''
        # create a new node from the Node class
        new_node = Node(data)
        # point the new node to the previous head, using its next_node property that comes from the class "Node"
        # if no previous node exists the next node will be "None"
        # self.head here is the existing linkedlist head
        new_node.next_node = self.head
        # set new node as the head of the list
        self.head = new_node

    def search(self,key):
        '''
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time
        '''
        current = self.head

        while current:
    
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


    def insert(self, data, index):
        '''
        Insert a new node containing data at a index position
        Insertion takes O(1) time 
        But finding the node at the insertion point takes O(n) time
        Adding both time complexities together gives O(n) time complexity altogether 
        '''

        if index == 0:
            # call the previous add function
            # this is the same as adding to the first node of the linkedlist
            self.add(data)
        if index > 0:
            # new element to be inserted anywhere apart from the  first node
            new_element = Node(data)

            # establish the position to insert  and where pointer begins on the list

            position = index
            current = self.head 

            # to insert the new node, the new node must point to the element at the insert index 
            # element previous to the new node index must point to the new node.
            # this while loop gets the index of the node just before the insert index
            # a new current node reference emerges after the while loop

            while position > 1:
                current = current.next_node
                position -= 1

            # name the current  node the previous node
            # The node after it set to  thre next_now_node

            prev_node  = current
            next_now_node = current.next_node

            # insert the new node between the previous and the next_now_node

            prev_node.next_node = new_element
            new_element.next_node = next_now_node


    def remove(self,key):

        # the remove method can be instatiated using either a key or an index
        # this rmove method is instatiated using a key

        # current points to the head
        current = self.head
        # previous element set to None
        previous_element = None
        # a found criteria sets to false
        found = False

        while current and not found:
            # if the element is at the beginning of our node
            if current.data == key and current == self.head:
                found = True
                # point the head to the next_node
                self.head = current.next_node 
            # if the element is at anywhere else
            elif current.data == key:
                found = True
                previous_element.next_node  = current.next_node
            
            else:
                # if the element is not found yet
                # set current to previous and current to the next_node.
                previous_element = current
                current = current.next_node

        # return the removed value
        return current
 

    def __repr__(self):
        '''
        Return the string representative of the list
        Takes O(n) time
        '''
        nodes = []
        current = self.head

        # this while loop traverse to the end of the array and ends when the current = "None"

        while current:
            # mark the end and return
            if current is self.head:
                nodes.append("[Head: %s" % current.data)
            # mark the tail and return
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            # return any other the way it is 
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return "-> ".join(nodes)


# calls

# checking the node class
N1 = Node(3) # create a node N1 with a value 3
N2 = Node(4) # create a node N2 with a value 4
N1.next_node = N2 # linking the node N1 and N2  together
N1.next_node  #calls the next node to N1

# connecting the Node class and the linkedList class

l = LinkedList() # create an instance of the linked_list
N1 = Node(10)     # create an instance  of the node 
l.head = N1       # composition : create an instance of the head in the linkedList and connecting it to the Node class
l.size()          # calling a method to work on the linked_list
