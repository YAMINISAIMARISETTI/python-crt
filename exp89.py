def findTotalCurtains(n,numbers):
    total=0
    for i in numbers:
        total+=i//12
    return total
n=int(input())
numbers=list(map(int,input().split()))
print(findTotalCurtains(n,numbers))