class Node:
    def __init__(self,value):
        self.value= value
        self.next = None
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def  addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
    
    # def removeNode(self, value): 
    #         runner = self.head
    #         runner = runner.next
    #         print(runner.next)
            

    #     while(runner.next != None):
    #         prev_runner = runner
    #         runner = runner.next 
    #     print(runner.next)


    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)

