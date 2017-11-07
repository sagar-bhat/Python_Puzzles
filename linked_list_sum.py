'''
A Linked List Implementation which
adds the value of two Linked lists.
Written By - Sagar Bhat

Input: Head of both Linked Lists
E.g.
List1: 1--2--3
List2: 1--0--6
Output: 321 + 601 = 922 i.e. 2--2--9

'''

def addList(head1,head2):

    # Variables to store length of two linked lists
    l1 = l2 = -1
    # Variables to store value retrieved from wo linked lists
    val1 = val2 = 0

    # Elements of First Linked List
    elem1 = []

    # Elements of Second Linked List
    elem2 = []

    current = head1
    while current!= None:
        l1 = l1 + 1
        elem1.append(current.value)
        current = current.next

    current = head2
    while current!= None:
        l2 = l2 + 1
        elem2.append(current.value)
        current = current.next 

    for x in reversed(elem1):
        val1 = val1 + (x)*(10**l1)
        l1 = l1 - 1

    for x in reversed(elem2):
        val2 = val2 + (x)*(10**l2)
        l2 = l2 - 1

    list3 = [int(i) for i in str(val1+val2)]

    return reversed(list3),(val1+val2)

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

    def forwardList(self):
        '''
        Prints the Linked List
        in Forward Manner.

        '''

	current=self.head
        print "\nLinkedList: "
	while current!=None:
	    print "{0}".format(current),
            current=current.next			

if __name__ == '__main__':

    list1 = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()

    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7]
    
    for x in l1:
        list1.insert(x)
    
    for x in l2:
        list2.insert(x)

    list1.forwardList()
    list2.forwardList()

    l3,val = addList(list1.head,list2.head)

    print "\nAddition of Two Linked Lists:",

    for x in l3:
        list3.insert(x)

    list3.forwardList()


