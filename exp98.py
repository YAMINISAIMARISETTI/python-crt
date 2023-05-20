n = int(input("enter a number: "))
if(n == 21):
    print("Sufficient lemons")
elif(n>21):
    print("we have extra",abs(21-n),"lemons")
else:
    print("we need",abs(21-n),"lemons")