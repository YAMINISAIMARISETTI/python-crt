class Dequeue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addRear(self, item):
        self.items.append(item)
        
    def addFront(self, item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.queue)

            
d = Dequeue()
d.isEmpty()
d.addRear(8)
d.addRear(55)
d.addFront()
d.addFront()