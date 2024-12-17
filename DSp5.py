def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
        if (j < i):
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def Quicksort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)
        Quicksort(arr, low, p - 1)
        Quicksort(arr, p + 1, high)

# Driver Code
n = int(input("\nHow many students are there?"))
arr = []
for i in range(0, n):
    item = float(input("\nEnter percentage marks"))
    arr.append(item)

print("You have entered following scores...\n")
print(arr)

print("\n The sorted Scores are...")
Quicksort(arr, 0, n - 1)
print(arr)
print("Top Five Scores are...")
for i in range(len(arr) - 1, len(arr) - 6, -1):
    print(arr[i])