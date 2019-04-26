class Node:
    def __init__(self,value):
        self.value = value
        self.next= None
class SList:
    def __init__(self, value):
        self.head = None
        
    def addNode(self, value):
        node = Node(value)
         
        if self.head == None:
            self.head = Node
        
        curr= self.head
        while(curr != None):
            curr = curr.next
        curr.next = node
        return self
        
    def remove_node(self,value):
        
            


    def printAllValues(self):
        if self.head  == None:
            print(None)
        else:
            curr = self.head
            result = []
            while(curr):
                result.append(curr.value)
                curr = curr.next

