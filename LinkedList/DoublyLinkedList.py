class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def printList(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head 
            while(temp):
                print(temp.data)
                temp = temp.next 
                
    def insertInEmptyList (self, data):
        if self.head is None:
            nodeToAdd = Node(data)
            self.head = nodeToAdd
            return
        else:
            print("This is list is not empty.")
            
    def insertAtHead(self,data):
        if self.head is None:
            self.insertInEmptyList(data)
        nodeToAdd = Node(data)
        nodeToAdd.next = self.head 
        self.head.prev = nodeToAdd
        self.head = nodeToAdd
    
    def insertAtTail(self,data):
        if self.head is None:
            self.insertInEmptyList(data)
        nodeToAdd = Node(data)
        temp = self.head 
        while(temp.next):
            temp = temp.next 
        temp.next = nodeToAdd
        nodeToAdd.prev = temp
    
    def insertAtNode(self,data,nodeData):
        if self.head is None:
            self.insertInEmptyList(data)
        nodeToAdd = Node(data)
        temp = self.head 
        while(temp.data != nodeData):
            temp = temp.next # this stops when temp is equal to the node after which we want to insert out new node 
        nextNode = temp.next # this keeps track of the node which is after our new node 
        #Making all the connections 
        temp.next = nodeToAdd
        nodeToAdd.prev = temp 
        nodeToAdd.next = nextNode
        nextNode.prev = nodeToAdd
        
    def removeAtHead(self):
        if self.head is None:
            print("This is an empty list")
        else:
            temp = self.head 
            self.head = temp.next 
    
    def removeAtTail(self):
        if self.head is None:
            print("This is an empty list")
        else:
            temp = self.head 
            while(temp.next):
                temp = temp.next # this stops at the last element of the list 
            temp.prev.next = None
    
    def removeAtNode(self,nodeData):
        if self.head is None:
            print("This is an empty list")
        else:
            temp = self.head 
            while(temp.data != nodeData):
                temp = temp.next # this stops at the node which we want to remove  
            temp.prev.next = temp.next 
            temp.next.prev = temp.prev 
    
    def contains(self,data):
        if self.head is None:
            print("This is an empty list, please insert some items.")
        else:
            temp = self.head 
            while(temp):
                if(temp.data == data):
                    return True
                else:
                    temp = temp.next 
            
            return False 
            
        
        
        
        
        
        
 
dLL = DoublyLinkedList()

dLL.insertInEmptyList(0)
dLL.insertAtTail(1)
dLL.insertAtTail(2)
dLL.insertAtTail(3)
dLL.insertAtTail(4)
dLL.insertAtTail(5)
dLL.insertAtTail(6)

#Works perfectly fine 

print("This is our list: \n")
dLL.printList()
