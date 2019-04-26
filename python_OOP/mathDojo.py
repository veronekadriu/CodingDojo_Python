# Creates a Python class called MathDojo that has the methods add and subtract.
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, *arg):
        self.result += sum(arg)
        return self

    def subtract(self, *arg):
        self.result -= sum(arg)
        return self
    
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
    
        
