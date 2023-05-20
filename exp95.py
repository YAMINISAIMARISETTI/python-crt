class SRMQueue:
    
    def __init__(self):
        self.queue = list()
        
    def add_element(self,val):
#Insert method to add element
        if val not in self.queue:
            #self.queue.insert(0,val)
            self.queue.append(val)
            return True
        return False

    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)
    def del_element(self):
        print("popped item: "+self.queue.pop(0))
        
        
q1 = SRMQueue()
q1.add_element("Diwali")
q1.add_element("Dhasara")
q1.add_element("X-Mas")
q1.add_element("Bakreeth")
q1.display()

q1.del_element()
q1.del_element()
q1.del_element()
q1.del_element()
q1.display()


print("The length of Queue: ",q1.size())        