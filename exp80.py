class abc():
    def __init__(self,var):
        self.var=var
        if(var%2==0):
            print("even")
        else:
            print("odd")
obj=abc(20)       