def FindLargestElement(arr,n):
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter elements of the array: ")
    for i in range(n):
        numbers = int(input())
        arr.append(numbers)
        maxVal = FindLargestElement(arr,n)
        print ("Largest in given array is",maxVal)
