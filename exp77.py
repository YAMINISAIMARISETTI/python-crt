#program to create self argument and access an object
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is",value)
obj=abc(100)