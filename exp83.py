class Number:
    def __init__(self,num):
        even = []
        odd = []
        self.num=num
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
n1=Number(11)
n2=Number(12)
n3=Number(13)
n4=Number(28)
n5=Number(7)
print("even number list is",Number.even)
print("odd number list is",Number.odd)
