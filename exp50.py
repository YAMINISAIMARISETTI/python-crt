term=int(input("Enter a number:"))
if term%2==0:
    term=term//2
    print(2*(term-1))
else:
    term=term//2+1
    print(1*(term-1))