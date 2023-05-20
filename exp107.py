def binary_search(Agelist,n):
    low = 0
    high = len(Agelist) - 1
    mid = 0
    while low <= high:
        mid = (high+low) // 2
        if Agelist[mid] < n:
            low = mid + 1
        elif Agelist[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
#Agelist=[110,240,150,350,750,250,550]
Agelist=[110,115,120,200,225,250,275,300]

n = 250

result = binary_search(Agelist,n)

if result != -1:
    print("Age is present at index:", str(result))
else:
    print("Age is not present in Agelist")