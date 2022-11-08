## Name:Umang
## Roll no : F098
import numpy as np
##6.1
arr = np.array([1, 2, 3, 4], ndmin=int(input("enter no")))
print(arr)
print('number of dimensions :', arr.ndim)

##6.2
arr = np.array([1, 2, 3, 4])

print(arr[0])

##6.3

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

##6.4

##aab tak question nai samja

##6.5
x = lambda a:[1,2,3,4,5,6]
print(x([]))

##6.6

## 6.6 ka alag file hai

##6.7
list=[10,20,4,45,99]
list.sort()
print("Largest no. is: ",list[-1])

##6.8
'''arr1 = np.array([10, 20, 30, 40])
print("array1 ", arr1)
  
arr2 = np.array([20, 40, 60, 80])
print("array2 ", arr2)
print("Union of two arrays :", np.union1d(arr1, arr2))
'''

##                                   OR



def union(list1, list2):
    # Make list1 and list2 as set
    list1 = set(list1)
    list2 = set(list2)

    # Print list1, list2
    print("List 1= ", list1)
    print("List 2= ", list2)

    # Using inbuilt function union print the result
    print("Union of two list: ", list1 | list2)


def intersection(list1, list2):
    # Make list1 and list2 as set
    list1 = set(list1)
    list2 = set(list2)

    # Using inbuilt function intersection print the result
    print("Intersection of two list: ", list1 & list2)


# Declare two empty list list1 and list2
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

# call the function union
union(list1, list2)

# call the function intersection
intersection(list1, list2)

