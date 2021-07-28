count = int(0)
n = int(input("Enter the number of test cases: "))
for _ in range(0, n):
    t = int(input("Enter the size of the array: "))
    arr = list(map(int, input("\n Enter the elements of the array: ").strip().split()))[:t]
    k = int(input("\n Enter the element you want to search: "))
    for x in range(0, t):
        count +=1
        if arr[x] == k:
            print("Yes the element is present in the array")

    print(f'The number of comparisons are: {count}')
