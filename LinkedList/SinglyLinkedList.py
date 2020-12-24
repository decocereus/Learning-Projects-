class Node:
    def __init__ (self,data = None ):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        printNode = self.head
        while printNode is not None:
            print(printNode.data)
            printNode = printNode.next 
    def insertInEmptyList(self,data):
        if self.head is None:
            nodeToAdd = Node(data)
            self.head = nodeToAdd
        else:
            print("List is not empty")
    
    def addNodeAtHead(self, data):
        nodeToAdd = Node(data)
        nodeToAdd.next = self.head
        self.head = nodeToAdd 
        
    def addNodeAtTail(self, data):
        if (self.head is None):
            nodeToAdd = Node(data)
            self.head = nodeToAdd
            return 
        else:
            nodeToAdd = Node(data)
            temp = self.head
            while(temp.next):
                temp = temp.next # this takes us to the last node in our list 
            temp.next = nodeToAdd
    
    def insterAtNode(self,data,p):
        if (self.head is None):
            self.addNodeAtHead(data)
        else:
            #Current list 7 0 1 2 10 
            nodeToAdd = Node(data)
            temp = self.head
            while(temp.next.data != p):
                temp = temp.next 
            temp = temp.next # This sets temp to the node after which we want to inster our new Node 
            nextNode = temp.next # This keeps track of the node which is after the new node 
            temp.next = nodeToAdd # here we assign the value of our next node to new node 
            nodeToAdd.next = nextNode # here we join the links back again 
            
    def contains(self, data):
        if self.head is None:
            print("This is an empty list, please insert some data.")
        else: 
            temp = self.head
            while(temp.next):
                if (temp.next.data == data):
                    return True
                else:
                    temp = temp.next 
            return False
        
    def removeAtHead(self):
        if self.head is None:
            print("This is an empty list, please insert some data.")
        else:
            self.head = self.head.next 
    
    def removeAtTail(self):
        if self.head is None:
            print("This is an empty list, please insert some data.")
        else:
            temp = self.head
            while temp.next is not None:
                newTail = temp # this follows the temp variable and stops at the second last position. 
                temp = temp.next 
            newTail.next = None  # Now to remove a node all we need is to sever the link between second last and last node 
    
    def removeAtNode(self,data):
        if (self.head is None):
            print("This is an empty list, please insert some data.")
        else:
            temp = self.head 
            while(temp.next.data != data):
                temp = temp.next 
            # 0 1 2 3 
            temp.next = temp.next.next # here our temp variable is at one, and we need to join 1 and 3, so temp.next.next is 3 
                   
    
                
    
            
       
linkedList = SinglyLinkedList()

linkedList.insertInEmptyList(0)

linkedList.addNodeAtTail(1)
linkedList.addNodeAtTail(2)
linkedList.addNodeAtTail(3)
linkedList.addNodeAtTail(4)
linkedList.addNodeAtTail(5)
linkedList.addNodeAtTail(6)
linkedList.addNodeAtTail(7)
linkedList.addNodeAtTail(8)
linkedList.addNodeAtTail(9)
linkedList.addNodeAtTail(10)

#Works perfectly fine.
    
print("This is our list\n")
linkedList.printList()



