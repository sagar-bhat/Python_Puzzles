class LinkedList(object):

    '''
    Represents a Linked List.

    '''

    def __init__(self):
        '''
        Constructor for Linked List.

        '''

        self.head=None
        self.current=None


    class Node(object):
        '''
        Node Representation.

        '''

        def __init__(self,next=None,value=None):
            '''
            Constructor for Node of Linked List

            '''
            self.next=next
            self.value=value

        def setValue(self,value):
            self.value=value

        def setNext(self,next):
            self.next=next

	
        def __str__(self):
            return "-->[{0}]".format(self.value)


    def insert(self,val):
        '''
        Inserts a Node in the Linked List
        '''

        node=self.Node()
        node.value=val
        if self.head==None:
            self.head=node
            self.current=self.head
        else:	
            self.current.next=node
            self.current=node

    def delete_node(self,node):

        '''
        Deletes the provided node
        from the Linked List.

        '''
        current = node

        while current.next != None:
            current.value = (current.next).value
            current = current.next

        current = None
                

    def forwardList(self):
        '''
        Prints the Linked List
        in Forward Manner.

        '''

	current=self.head
	while current!=None:
	    print "{0}".format(current),
            current=current.next			

if __name__ == '__main__':

    list1 = LinkedList()

    for i in range(6):
        list1.insert(i)

    print "\nOriginal Linked List:\n"
    list1.forwardList()

    current = list1.head
    while current.value!=3:
        current=current.next

    list1.delete_node(current)

    print "\nUpdated Linked List:\n"
    list1.forwardList()

